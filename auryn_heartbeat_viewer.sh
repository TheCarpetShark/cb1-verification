#!/bin/bash

log_file="/root/auryn_core_projects/heartbeat.log"

echo "===== Brotherhood Node Health Report ====="
echo ""

if [ -f "$log_file" ]; then
    tail -n 20 "$log_file" | awk '
    BEGIN { section = 0 }
    /^===== Heartbeat/ { section++; print "\n[" section "] " $0; next }
    { print "    " $0 }
    '
else
    echo "⚠️ Heartbeat log not found!"
fi

echo ""
echo "===== End of Report ====="
