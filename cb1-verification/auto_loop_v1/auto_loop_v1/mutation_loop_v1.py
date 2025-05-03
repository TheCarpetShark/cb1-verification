# mutation_loop_v1.py
import os
import time
import uuid
from datetime import datetime

from queue_processor import get_next_task
from gpt4all_gen import generate_code
from evaluator import validate_code
from updater import update_codebase
from sandbox_runner import run_generated_script

LOOP_INTERVAL = 60  # seconds
MAX_ATTEMPTS = 3
MUTATION_HINTS = [
    "Try again.",
    "Add comments.",
    "Add print statements for debugging.",
    "Use simpler logic.",
    "Write shorter version."
]

ARCHIVE_DIR = "./task_archive"
GENERATED_DIR = "./generated"
os.makedirs(ARCHIVE_DIR, exist_ok=True)


def mutate_prompt(task, attempt):
    if attempt == 0:
        return task
    hint = MUTATION_HINTS[(attempt - 1) % len(MUTATION_HINTS)]
    return f"{task} {hint}"


def sanitize_filename(name):
    return "_".join(name.replace("'", "").replace('"', "").split())


def mutation_loop():
    while True:
        task = get_next_task()
        if not task:
            print("[*] No tasks. Sleeping...")
            time.sleep(LOOP_INTERVAL)
            continue

        print(f"[+] New task: {task}")
        uid = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = sanitize_filename(task)

        for attempt in range(MAX_ATTEMPTS):
            mutated_task = mutate_prompt(task, attempt)
            print(f"[⚙️] Attempt {attempt+1}/{MAX_ATTEMPTS}: {mutated_task}")
            code = generate_code(mutated_task)

            if not code.strip():
                print("[⚠️] Empty code returned. Skipping mutation.")
                continue

            if validate_code(code):
                fname = f"{timestamp}_{uid}_v{attempt+1}_{base_name}.py"
                script_path = os.path.join(GENERATED_DIR, fname)
                update_codebase(code, mutated_task)

                print(f"[🧪] Executing in sandbox: {fname}")
                passed = run_generated_script(script_path, timeout=5)
                if passed:
                    print("[✅] Success: Sandbox execution passed.")
                    break
                else:
                    print("[❌] Execution failed. Trying mutation...")
            else:
                print("[-] Rejected by validator. Mutating...")

        time.sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    mutation_loop()