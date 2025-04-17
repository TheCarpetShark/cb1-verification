from gpt4all import GPT4All
from datetime import datetime
import json

QUEUE_PATH = "auryn.queue.json"
LOG_PATH = "auryn_queue.log"
MODEL_PATH = r"D:\NEURAL_CORE\auryn_core\models\deepseek-llama-8b.q4_0.gguf"

def load_queue():
    try:
        with open(QUEUE_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def save_queue(queue):
    with open(QUEUE_PATH, "w") as f:
        json.dump(queue, f, indent=2)

def append_task(task):
    queue = load_queue()
    queue.append({"task": task})
    save_queue(queue)

def log_message(message):
    with open(LOG_PATH, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def autopilot():
    queue = load_queue()
    task_list = "\n".join([f"- {t['task']}" for t in queue])

    prompt = f"""
You are Auryn, a local AI overseeing system automation.

Current task list:
{task_list}

Output one single-line task command. Do not explain. Do not use quotes. Do not include XML, HTML, or formatting. Return only the raw task as text.

"""

    model = GPT4All(MODEL_PATH, allow_download=False)

    with model:
        suggestion = model.generate(prompt, max_tokens=100)
        cleaned = suggestion.strip().split('\n')[0]
        append_task(cleaned)
        log_message(f"Suggested task: {cleaned}")

if __name__ == "__main__":
    autopilot()
