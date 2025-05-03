import json
import os
from datetime import datetime

QUEUE_FILE = "cccp.queue.json"
LOG_FILE = "cccp_executor.log"

def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)

def log_action(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def execute_task(task):
    log_action(f"Executed (stub): {task}")

def run():
    queue = load_queue()
    for task in queue:
        if "executed" not in task:
            execute_task(task["task"])
            task["executed"] = True
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

if __name__ == "__main__":
    run()
