from flask import Flask, request, render_template_string
import json
import os

app = Flask(__name__)
QUEUE_FILE = "cccp.queue.json"

def load_queue():
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    return []

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

@app.route("/", methods=["GET"])
def index():
    tasks = load_queue()
    html_tasks = "<br>".join(f"- {t['task']}" for t in tasks)
    return render_template_string(open("html_ui/index.html", encoding="utf-8").read(), tasks=html_tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        queue = load_queue()
        queue.append({"task": task})
        save_queue(queue)
    return index()

if __name__ == "__main__":
    app.run(port=7860, debug=True)
