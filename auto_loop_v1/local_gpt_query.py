# local_gpt_query.py
import sys
from gpt4all import GPT4All

# Path to your model directory and filename
MODEL_NAME = "DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf"
MODEL_PATH = "D:/NEURAL_CORE/auryn_core/models"

# Grab the prompt from the command line args
prompt = sys.argv[1]

# Load the model
model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_PATH)

# Run the model and capture response
response = model.prompt(prompt, max_tokens=512, temp=0.7)

# Output response to STDOUT for the loop to capture
print(response)
