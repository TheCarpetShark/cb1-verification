from gpt4all import GPT4All

# Using raw string to handle Windows path safely
model_path = r"D:\NEURAL_CORE\auryn_core\models\deepseek-llama-8b.q4_0.gguf"

model = GPT4All(model_name=model_path, allow_download=False)

response = model.chat_completion(
    "You are a helpful assistant. What is the Brotherhood Construct?",
    verbose=True
)

print(response['choices'][0]['message']['content'])
