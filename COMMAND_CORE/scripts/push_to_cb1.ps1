# Define paths
$localPath = "D:\NEURAL_CORE\auryn_core\PROJECTS\*"   # <-- Adjust if needed
$remotePath = "/root/auryn_core_projects/"            # <-- Destination on CB1
$cb1_ip = "192.168.1.216"
$username = "root"

# Check if SCP is available
if (-not (Get-Command scp.exe -ErrorAction SilentlyContinue)) {
    Write-Host "Error: 'scp.exe' not found. Please install OpenSSH client tools from Windows features."
    exit
}

# Properly build SCP command using `${}` around variables
$scpCommand = "scp -r `"$localPath`" ${username}@${cb1_ip}:`"$remotePath`""

# Execute SCP as external command (so PowerShell does NOT try to parse it)
cmd /c $scpCommand
