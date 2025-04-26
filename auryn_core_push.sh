#!/bin/bash

cd /root/auryn_core_projects || exit 1

# Add all changes
git add .

# Commit changes with timestamp
commit_message="Auto-commit from CB1 at $(date +"%Y-%m-%d %H:%M:%S")"
git commit -m "$commit_message"

# Push to GitHub
git push origin master
