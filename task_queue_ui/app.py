from flask import Flask, render_template, request, jsonify
from queue_handler import load_tasks, save_tasks, add_task, delete_task, update_task

app = Flask(__name__)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def post_task():
    content = request.json.get("content")
    return jsonify(add_task(content))

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    return jsonify(delete_task(task_id))

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    new_content = request.json.get("content")
    return jsonify(update_task(task_id, new_content))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
