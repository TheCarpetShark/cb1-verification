#!/bin/bash

log_file="/root/auryn_core_projects/critical_alerts.log"
timestamp=$(date)

# Check heartbeat
if [ ! -f "/root/auryn_core_projects/heartbeat.log" ]; then
    echo "[$timestamp] CRITICAL: Heartbeat log missing!" >> "$log_file"
fi

# Check codex
if [ ! -f "/root/BROTHERHOOD_CODEX.txt" ]; then
    echo "[$timestamp] CRITICAL: Codex file missing!" >> "$log_file"
fi
