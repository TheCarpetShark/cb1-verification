# Auto-generated GPU Llama Launch Script
cd "D:\NEURAL_CORE\auryn_core\llama_gpu"

# Assuming server.exe (GPU build of llama.cpp) exists here
.\server.exe --model ..\models\your_model.gguf --n-gpu-layers 50 --ctx-size 4096 --threads 8 --port 5000
