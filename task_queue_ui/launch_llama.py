from gpt4all import GPT4All

model_path = r"D:\NEURAL_CORE\auryn_core\models\deepseek-llama-8b.q4_0.gguf"
model = GPT4All(model_path, allow_download=False)

with model:
    response = model.chat("What is the Brotherhood Construct?")
    print(response)
