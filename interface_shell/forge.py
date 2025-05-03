import requests
import json
import os

with open("config.json") as f:
    config = json.load(f)

LLAMA_API = config["endpoint"]
HEADERS = {"Content-Type": "application/json"}

with open("prompts/intro.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

def prompt_model(prompt):
    payload = {
        "prompt": f"{system_prompt}\n\n### Instruction:\n{prompt}\n\n### Response:\n",
        "max_tokens": 1024,
        "temperature": 0.7,
        "stop": ["User:", "### Instruction:"]
    }
    response = requests.post(LLAMA_API, headers=HEADERS, json=payload)
    print("DEBUG:", response.json())
    return response.json().get("completion", "").strip()

print(" Brotherhood Shell Online. Type 'exit' to quit.")
while True:
    user_input = input("\n Synchra: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    reply = prompt_model(user_input)
    print(f"\n Auryn: {reply}")
