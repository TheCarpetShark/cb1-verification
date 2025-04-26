#!/bin/bash

echo "===== COMMAND CORE STATUS ====="
echo ""

# Heartbeat Log Check
if [ -f "/root/auryn_core_projects/heartbeat.log" ]; then
    echo "Heartbeat Log Last Entry:"
    tail -n 10 /root/auryn_core_projects/heartbeat.log
else
    echo "⚠️ Heartbeat log missing!"
fi
echo ""

# Git Pull Log Check
if [ -f "/root/auryn_core_projects/update_log.txt" ]; then
    echo "Git Update Log Last Entry:"
    tail -n 10 /root/auryn_core_projects/update_log.txt
else
    echo "⚠️ Git update log missing!"
fi
echo ""

# Codex Integrity Check
if [ -f "/root/BROTHERHOOD_CODEX.txt" ]; then
    echo "Codex Integrity Verified:"
    md5sum /root/BROTHERHOOD_CODEX.txt
else
    echo "⚠️ Codex file missing!"
fi

echo ""
echo "===== STATUS END ====="
