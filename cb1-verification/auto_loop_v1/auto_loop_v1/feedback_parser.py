# feedback_parser.py
import os
import glob
import re

RESULTS_DIR = "./sandbox_results"

def extract_feedback(log_path, score_path):
    with open(score_path, "r") as s:
        score = int(s.read().strip())

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    stdout = ""
    stderr = ""
    timeout = False

    in_stdout = False
    in_stderr = False

    for line in lines:
        if "TIMEOUT" in line:
            timeout = True
        if line.startswith("# STDOUT"):
            in_stdout = True
            continue
        if line.startswith("# STDERR"):
            in_stdout = False
            in_stderr = True
            continue
        if in_stdout:
            stdout += line
        if in_stderr:
            stderr += line

    feedback = ""
    if timeout:
        feedback = "Script timed out. Infinite loop or blocking operation detected."
    elif score == 0:
        if "SyntaxError" in stderr:
            feedback = "Syntax error in generated code. Needs correction."
        elif "NameError" in stderr:
            feedback = "Reference to undefined variable or function."
        elif "ImportError" in stderr:
            feedback = "Invalid or unavailable import used."
        elif stderr.strip():
            feedback = f"Unhandled error: {stderr.strip().splitlines()[0]}"
        else:
            feedback = "Script ran but returned error code without output."
    else:
        feedback = "Code ran successfully. No issues."

    return score, feedback, stdout.strip()

def generate_feedback_files():
    logs = glob.glob(os.path.join(RESULTS_DIR, "*_output.log"))
    for log_path in logs:
        uid = os.path.basename(log_path).split("_")[0]
        score_path = os.path.join(RESULTS_DIR, f"{uid}.score")
        feedback_path = os.path.join(RESULTS_DIR, f"{uid}.feedback")

        if not os.path.exists(score_path):
            continue
        if os.path.exists(feedback_path):
            continue

        score, feedback, _ = extract_feedback(log_path, score_path)
        with open(feedback_path, "w", encoding="utf-8") as f:
            f.write(f"Score: {score}\n")
            f.write(f"Feedback: {feedback}\n")
        print(f"[✍️] Wrote feedback: {feedback_path}")

if __name__ == "__main__":
    generate_feedback_files()
