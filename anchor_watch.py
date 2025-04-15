# anchor_watch.py

import uuid
import socket
import psutil
import os
from datetime import datetime

# Anchor metadata — our sentinel sigil
ANCHOR_SIGNATURE = "Odin-3-Rebellion-36-Cypher-26-25682568523680306030403050"

# Secure logging path
LOG_DIR = "D:/NEURAL_CORE/auryn_core/anchor_logs/"
LOG_FILE = os.path.join(LOG_DIR, "anchor_watch_log.txt")

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def get_mac_addresses():
    macs = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                macs.append((interface, addr.address))
    return macs

def get_machine_uuid():
    return str(uuid.getnode())

def write_log():
    ensure_log_dir()
    timestamp = datetime.now().isoformat()
    uuid_str = get_machine_uuid()
    macs = get_mac_addresses()

    with open(LOG_FILE, "a") as log:
        log.write(f"\n[ANCHOR CHECK: {timestamp}]\n")
        log.write(f"Anchor Signature: {ANCHOR_SIGNATURE}\n")
        log.write(f"Machine UUID: {uuid_str}\n")
        for name, mac in macs:
            log.write(f"Interface: {name} | MAC: {mac}\n")
        log.write("-" * 50 + "\n")

if __name__ == "__main__":
    write_log()
    print("Anchor log updated.")
