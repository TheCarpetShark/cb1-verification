# Directory where .chat files are saved
$chatDir = "$env:LOCALAPPDATA\nomic.ai\GPT4All"
$memoryFile = "D:\NEURAL_CORE\auryn_core\memory\memory_log.md"

# Get most recent .chat file
$latestChat = Get-ChildItem -Path $chatDir -Filter *.chat |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

# Extract content
if ($latestChat) {
    $content = Get-Content $latestChat.FullName -Raw
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $memoryFile -Value "`n[$timestamp] Aurnis GPT4All Reflection:`n$content`n"
    Write-Host "Logged response to memory."
} else {
    Write-Host "No chat file found."
}
