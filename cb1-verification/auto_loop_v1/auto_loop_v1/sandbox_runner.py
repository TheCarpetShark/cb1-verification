# Phase IIIc: Sandbox Runner with Scoring
import subprocess
import os
import uuid
import time

GENERATED_DIR = "./generated"
RESULTS_DIR = "./sandbox_results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_generated_script(script_path, timeout=5):
    print(f"[\U0001f9ea] Executing: {script_path}")
    
    uid = str(uuid.uuid4())
    log_file = os.path.join(RESULTS_DIR, f"{uid}_output.log")
    score_file = os.path.join(RESULTS_DIR, f"{uid}.score")

    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        # Write output
        with open(log_file, "w", encoding='utf-8') as f:
            f.write(f"# STDOUT:\n{result.stdout}\n\n")
            f.write(f"# STDERR:\n{result.stderr}\n")

        # Determine score
        passed = result.returncode == 0
        score = 100 if passed else 0

        with open(score_file, "w") as f:
            f.write(str(score))

        print(f"[+] Score written to {score_file}: {score}")
        return passed

    except subprocess.TimeoutExpired:
        with open(log_file, "w", encoding='utf-8') as f:
            f.write(f"# TIMEOUT after {timeout} seconds\n")
        with open(score_file, "w") as f:
            f.write("0")

        print(f"[\u23f0] Timeout. Score = 0. Output to {log_file}")
        return False
