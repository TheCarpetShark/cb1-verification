#!/bin/bash

cd /root/auryn_core_projects || exit 1

# Stage all changes
git add .

# Commit changes if there are any
if ! git diff --cached --quiet; then
    commit_message="Auto-commit from CB1 at $(date +"%Y-%m-%d %H:%M:%S")"
    git commit -m "$commit_message"
else
    echo "No changes to commit."
fi

# Push to GitHub
git push origin master
