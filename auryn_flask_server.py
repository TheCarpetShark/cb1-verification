from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os
import json
import ctypes
from llama_cpp import Llama

# Manually inject DLL path for llama-cpp (updated MSVC version)
dll_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.43.34808\bin\Hostx64\x64"
if not os.path.exists(dll_path):
    raise FileNotFoundError(f"Critical DLL directory not found: {dll_path}")
ctypes.windll.kernel32.SetDllDirectoryW(dll_path)

app = Flask(__name__, template_folder="cb1-verification/task_queue_ui/templates")

MEMORY_LOG_PATH = "Memory/auryn_mem_training.jsonl"
MODEL_PATH = "models/DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf"

# Load LLaMA model once at startup
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=8,
    use_mlock=True,
    verbose=False
)

@app.route("/")
def interface():
    return render_template("index.html")

@app.route("/auryn-query", methods=["POST"])
def handle_query():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = llm(prompt)
    answer = response["choices"][0]["text"].strip()

    # Save conversation memory
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": answer
    }
    with open(MEMORY_LOG_PATH, "a", encoding="utf-8") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
