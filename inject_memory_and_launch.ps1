# Path to seed file
$seedPath = "D:\NEURAL_CORE\auryn_core\memory\memory_log.md"

# Load contents
$memorySeed = Get-Content $seedPath -Raw

# Copy to clipboard
Set-Clipboard -Value $memorySeed
Write-Host "[AURNIS] Memory contents injected to clipboard."

# Launch GPT4All GUI
Start-Process "D:\GPT4ALL\bin\chat.exe"
Write-Host "[AURNIS] GPT4All GUI launched. Paste seed manually as first message."
