#!/bin/bash

# Define backup targets
backup_root="/mnt/1TB_SD_CARD/backups_cb1"
timestamp=$(date +"%Y%m%d_%H%M%S")
backup_file="$backup_root/auryn_core_cb1_backup_$timestamp.tar.gz"

# Ensure backup directory exists
mkdir -p "$backup_root"

# Create compressed snapshot
tar -czf "$backup_file" /root/auryn_core_projects

echo "Snapshot created at $backup_file"
