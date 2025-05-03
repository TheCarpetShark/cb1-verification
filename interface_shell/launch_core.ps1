# === AURYN CORE LAUNCHER ===

Write-Host "`n Preparing Auryn Core Launcher..."

# Detect threads
$cpuCores = [System.Environment]::ProcessorCount
$threads = if ($cpuCores -gt 16) { 16 } else { $cpuCores }
$nGpuLayers = 40

# Model & server paths
$modelPath = "D:\NEURAL_CORE\auryn_core\models\WizardCoder-Python-13B-V1.0.Q4_0.gguf"
$serverPath = "D:\NEURAL_CORE\auryn_core\dependencies\llama.cpp\build\bin\Release\llama-server.exe"

# Build args string for llama-server
$args = "--model `"$modelPath`" --port 5000 --ctx-size 8192 --n-gpu-layers $nGpuLayers --threads $threads"

# Launch server
Write-Host " Launching llama-server..."
Start-Process -FilePath $serverPath -ArgumentList $args

# Wait hardcoded 30 seconds for model to load
Write-Host " Waiting 30 seconds for model to bind to port 5000..."
Start-Sleep -Seconds 30

# Then poll until port is open
Write-Host " Checking port 5000 readiness..."
do {
    Start-Sleep -Milliseconds 500
    $portOpen = Test-NetConnection -ComputerName localhost -Port 5000 | Select-Object -ExpandProperty TcpTestSucceeded
} until ($portOpen)

Write-Host " Server ready. Launching Interface..."

# Run the Python shell
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "forge.py" -WorkingDirectory "D:\NEURAL_CORE\auryn_core\interface_shell"
