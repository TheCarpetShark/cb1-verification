# loop_engine_v2.py
import time
import os
import re
import uuid
from datetime import datetime

from queue_processor import get_next_task
from gpt4all_gen import generate_code
from evaluator import validate_code
from updater import update_codebase
from sandbox_runner import run_generated_script

LOOP_INTERVAL = 60
GENERATED_DIR = "./generated"
ARCHIVE_DIR = "./task_archive"
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

while True:
    task = get_next_task()
    if task:
        print(f"[+] Task Detected: {task}")
        code = generate_code(task)

        if not code.strip():
            print("[⚠️] No code generated. Skipping task.")
            continue

        # Archive task prompt
        uid = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_task = sanitize_filename(task.replace(' ', '_'))
        script_filename = f"{timestamp}_{safe_task}.py"
        script_path = os.path.join(GENERATED_DIR, script_filename)
        archive_path = os.path.join(ARCHIVE_DIR, f"{timestamp}_{safe_task}.task")

        with open(archive_path, "w", encoding="utf-8") as f:
            f.write(task)

        if validate_code(code):
            update_codebase(code, task)

            print(f"[🧪] Executing in sandbox: {script_path}")
            passed = run_generated_script(script_path, timeout=5)

            if passed:
                print("[✅] Code passed sandbox execution.")
            else:
                print("[❌] Code failed execution.")
        else:
            print("[-] Code rejected due to failed validation.")
    else:
        print("[*] No tasks. Sleeping...")

    time.sleep(LOOP_INTERVAL)