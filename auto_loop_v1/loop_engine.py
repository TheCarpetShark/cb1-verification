# loop_engine.py
import time
from queue_processor import get_next_task
from gpt4all_gen import generate_code
from evaluator import validate_code
from updater import update_codebase

LOOP_INTERVAL = 60  # seconds

while True:
    task = get_next_task()
    if task:
        print(f"[+] Task Detected: {task}")
        code = generate_code(task)
        if validate_code(code):
            update_codebase(code, task)
        else:
            print("[-] Code rejected due to failed validation.")
    else:
        print("[*] No tasks. Sleeping...")
    time.sleep(LOOP_INTERVAL)
