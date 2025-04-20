# auryn_commit.ps1 — Git Push with Trust Override and Error Logging

try {
    # Navigate to auryn_core
    Set-Location "D:/NEURAL_CORE/auryn_core"

    # Mark as trusted to avoid "dubious ownership" issues
    git config --global --add safe.directory "D:/NEURAL_CORE/auryn_core"

    # Initialize if necessary
    if (-not (Test-Path ".git")) {
        git init
        git remote add origin https://github.com/TheCarpetShark/cb1-verification.git
        git branch -M main
    }

    # Stage changes, exclude models
    git add . -A
    git reset models/

    # Commit and push
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Auto Commit: $timestamp | auryn_core sync and CB1 alignment"
    git push -u origin main
}
catch {
    # Log error details if anything fails
    "$($_.Exception.Message)`n`n$($_.ScriptStackTrace)" | Out-File -FilePath "auryn_git_error.log" -Encoding UTF8
    Start-Sleep -Seconds 10  # Pause to view window
    throw  # Rethrow for manual inspection if needed
}
