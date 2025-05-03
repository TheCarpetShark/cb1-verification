# queue_processor.py
import os

QUEUE_DIR = "./queue"
os.makedirs(QUEUE_DIR, exist_ok=True)

QUEUE_DIR = "./queue"

def get_next_task():
    files = sorted(f for f in os.listdir(QUEUE_DIR) if f.endswith(".task"))
    if files:
        with open(os.path.join(QUEUE_DIR, files[0]), 'r') as f:
            task = f.read().strip()
        os.remove(os.path.join(QUEUE_DIR, files[0]))
        return task
    return None
