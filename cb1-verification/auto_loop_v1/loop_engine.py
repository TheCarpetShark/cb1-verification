# loop_engine.py
import time
from queue_processor import get_next_task
from gpt4all_gen import generate_code
from evaluator import validate_code
from updater import update_codebase
from sandbox_runner import run_generated_script
import os
from datetime import datetime
import re

LOOP_INTERVAL = 60  # seconds

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

        if validate_code(code):
            # Prepare file path before saving
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_task = sanitize_filename(task.replace(' ', '_'))
            script_path = f"./generated/{timestamp}_{safe_task}.py"

            update_codebase(code, task)

            # Phase III: Execute in sandbox
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
    from feedback_parser import generate_feedback_files
    generate_feedback_files()
