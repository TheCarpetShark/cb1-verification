import os
import subprocess
import json
from datetime import datetime

QUEUE_FILE = "/root/cb1_github_repo/auryn.queue.json"
LOG_FILE = "/root/cb1_github_repo/auryn_queue.log"

def log(msg):
    try:
        with open(LOG_FILE, "a") as log_file:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            log_file.write(f"{timestamp} {msg}\n")
        print(msg)
    except Exception as e:
        print(f"[LOGGING FAILURE] {e}")

log("=== Aurnis Daemon Triggered ===")

def run_script(script_name):
    try:
        result = subprocess.run(["python3", script_name], capture_output=True, text=True)
        log(f"Executed {script_name}:\n{result.stdout}")
    except Exception as e:
        log(f"Error running {script_name}: {e}")

def git_commit(message):
    try:
        os.chdir("/root/cb1_github_repo")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        log(f"Committed and pushed to GitHub: {message}")
    except Exception as e:
        log(f"Git error: {e}")

def reboot():
    log("System reboot triggered.")
    subprocess.run(["reboot"])

def process_json_queue():
    if not os.path.exists(QUEUE_FILE):
        log("No JSON queue file found.")
        return

    try:
        with open(QUEUE_FILE, "r") as f:
            commands = json.load(f)
    except Exception as e:
        log(f"Failed to load JSON queue: {e}")
        return

    for item in commands:
        command = item.get("command")
        arg = item.get("args", "")

        if command == "run_script":
            run_script(arg)
        elif command == "git_commit":
            git_commit(arg)
        elif command == "reboot":
            reboot()
        else:
            log(f"Unknown command in JSON: {item}")

    os.remove(QUEUE_FILE)
    log("JSON queue processed and cleared.")

if __name__ == "__main__":
    process_json_queue()
