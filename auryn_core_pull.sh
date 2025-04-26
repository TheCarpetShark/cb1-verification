#!/bin/bash

cd /root/auryn_core_projects || exit 1

# Pull latest updates
git pull origin master >> /root/auryn_core_projects/update_log.txt 2>&1

# Timestamp the update
echo "Pulled at \$(date)" >> /root/auryn_core_projects/update_log.txt
