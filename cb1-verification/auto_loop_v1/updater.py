from datetime import datetime
import os
import re

SAVE_DIR = "./generated"

def sanitize_filename(name):
    # Remove forbidden characters for Windows filenames
    return re.sub(r'[<>:"/\\|?*]', '', name)

def update_codebase(code, task_desc):
    os.makedirs(SAVE_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_task = sanitize_filename(task_desc.replace(' ', '_'))
    filename = f"{SAVE_DIR}/{timestamp}_{safe_task}.py"

    print(f"[DEBUG] Writing code to file: {filename}")
    print(f"[DEBUG] Code content preview:\n{code[:100]}...")

    with open(filename, "w", encoding='utf-8') as f:
        f.write(code)
    print(f"[+] Code committed to: {filename}")
