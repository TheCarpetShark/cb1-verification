#!/bin/bash

log_file="/root/auryn_core_projects/heartbeat.log"

echo "===== Heartbeat at \$(date) =====" >> \$log_file
uptime >> \$log_file
free -h >> \$log_file
df -h / >> \$log_file
echo "" >> \$log_file
