from gpt4all import GPT4All
from datetime import datetime
import json
import os

QUEUE_FILE = "cccp.queue.json"
LOG_FILE = "cccp_autopilot.log"
MODEL_PATH = r"D:\NEURAL_CORE\models\DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf"

def load_queue():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def log_entry(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def autopilot():
    queue = load_queue()
    task_list = "\n".join([f"- {entry['task']}" for entry in queue])
    
    prompt = f"""
You are a sovereign AI assistant overseeing task automation.
These are your current tasks:
{task_list}

Respond ONLY with one new task to append to the list.
Do not explain, justify, or add anything extra.
Output a single line task only.
    """

    model = GPT4All(model_name=MODEL_PATH, allow_download=False)
    response = model.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        verbose=True
    )

    if 'choices' in response:
        task = response['choices'][0]['message']['content'].strip()
        log_entry(f"Generated Task: {task}")
        queue.append({"task": task})
        save_queue(queue)

if __name__ == "__main__":
    autopilot()
