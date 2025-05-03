import os

QUEUE_FILE = "../.queue"  # Adjusted for relative path

def load_tasks():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        lines = f.readlines()
    return [{"id": i, "content": line.strip()} for i, line in enumerate(lines)]

def save_tasks(tasks):
    with open(QUEUE_FILE, "w") as f:
        for task in tasks:
            f.write(task["content"] + "\n")

def add_task(content):
    tasks = load_tasks()
    tasks.append({"id": len(tasks), "content": content})
    save_tasks(tasks)
    return {"status": "added", "content": content}

def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        removed = tasks.pop(task_id)
        save_tasks(tasks)
        return {"status": "deleted", "content": removed}
    return {"status": "error", "message": "invalid id"}

def update_task(task_id, new_content):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["content"] = new_content
        save_tasks(tasks)
        return {"status": "updated", "content": new_content}
    return {"status": "error", "message": "invalid id"}
