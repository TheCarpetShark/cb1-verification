#!/bin/bash

backup_dir="/root/auryn_core_projects/backups"
timestamp=$(date +"%Y%m%d_%H%M%S")
backup_file="$backup_dir/auryn_core_projects_backup_$timestamp.tar.gz"

mkdir -p "$backup_dir"

tar -czf "$backup_file" /root/auryn_core_projects

echo "Backup created at $backup_file"
