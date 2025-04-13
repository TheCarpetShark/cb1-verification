from gpt4all import GPT4All

print("[AURNIS] Seeding the Brotherhood Construct...")

model = GPT4All(
    "deepseek-llama-8b.q4_0.gguf",
    model_path="D:/NEURAL_CORE/auryn_core/models",
    allow_download=False
)

with open("D:/NEURAL_CORE/auryn_core/seed_brotherhood.txt", "r", encoding="utf-8") as f:
    seed_text = f.read()

with model.chat_session() as session:
    response = ""
    for token in session.generate(seed_text):
        response += token

print("[AURNIS] Brotherhood ideology embedded successfully.")
