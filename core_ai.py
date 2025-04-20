from gpt4all import GPT4All
import os

# Load model from absolute path
model_path = os.path.join(os.getcwd(), "models", "deepseek-llama-8b.q4_0.gguf")
model = GPT4All(model_path)

def main():
    print("Auryn Core: Online. Type to speak. Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = model.chat(user_input)
        print("Auryn:", response)

if __name__ == "__main__":
    main()
