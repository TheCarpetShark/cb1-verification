
# auryn_sync.ps1 - Upload auryn_core to CB1 via SCP, excluding large/unnecessary dirs

$source = "D:\NEURAL_CORE\auryn_core"
$archive = "D:\NEURAL_CORE\auryn_core_upload.zip"
$cb1_dest = "root@192.168.1.216:/root/"
$extract_path = "/root/auryn_core"

# Clean up old zip if it exists
if (Test-Path $archive) { Remove-Item $archive }

# Exclude rules
$exclude = @("*.log", "*.pyc", "__pycache__", "venv", "models", ".git")

# Gather files to include
$files = Get-ChildItem -Recurse -Path $source | Where-Object {
    $relPath = $_.FullName.Substring($source.Length + 1)
    $exclude -notcontains $relPath.Split("\")[0] -and
    $exclude -notcontains $_.Name
}

# Compress filtered files
$files | Compress-Archive -DestinationPath $archive

# Upload using SCP
scp $archive $cb1_dest

Write-Host "Upload complete. Now SSH into the CB1 and extract:"
Write-Host "    unzip auryn_core_upload.zip -d $extract_path"
