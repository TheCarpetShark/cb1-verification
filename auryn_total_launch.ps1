# ========================
# AURYN TOTAL LAUNCHER
# ========================
$ErrorActionPreference = "Stop"

# === CONFIG ===
$venvPath = "D:\NEURAL_CORE\auryn_core\venv\Scripts\Activate.ps1"
$repoPath = "D:\NEURAL_CORE\auryn_core"
$model = "DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf"  # Set default here
$modelPath = "D:\NEURAL_CORE\auryn_core\models\$model"
$logFile = "D:\NEURAL_CORE\auryn_core\launch_log.txt"
$cb1Remote = "auryncb1:/home/auryncb1core"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# === STEP 1: Activate Virtual Environment ===
Write-Host "`n[$timestamp] Activating venv..." | Tee-Object -Append -FilePath $logFile
. $venvPath

# === STEP 2: Launch Model (llama.cpp backend assumed) ===
Set-Location -Path "D:\NEURAL_CORE\auryn_core"
Write-Host "Launching model: $model" | Tee-Object -Append -FilePath $logFile
python .\llama_gpu\main.py --model $modelPath --n-gpu-layers 35 --threads 10 --n-predict 512

# === STEP 3: Launch server queue or Flask (optional stub) ===
# Write-Host "Starting auryn queue handler..." | Tee-Object -Append -FilePath $logFile
# python auryn_queue_handler.py

# === STEP 4: Git Sync to CB1 ===
Write-Host "`nCommitting and pushing to CB1 Git repo..." | Tee-Object -Append -FilePath $logFile
cd $repoPath
git add .
git commit -m "Automated sync from auryn_total_launch @ $timestamp"
git push origin main --force

# === STEP 5: Final Log ===
Write-Host "`n[$timestamp] Launch Complete." | Tee-Object -Append -FilePath $logFile
