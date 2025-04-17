# score_exporter.py
import os
import glob
import csv
import re

RESULTS_DIR = "./sandbox_results"
CSV_PATH = os.path.join(RESULTS_DIR, "score_log.csv")


def extract_metadata(log_path, score_path, feedback_path):
    uid = os.path.basename(log_path).split("_")[0]
    timestamp_match = re.search(r"(\d{8}_\d{6})", log_path)
    timestamp = timestamp_match.group(1) if timestamp_match else "unknown"

    try:
        with open(score_path, "r") as sf:
            score = int(sf.read().strip())
    except:
        score = -1

    try:
        with open(feedback_path, "r", encoding="utf-8") as ff:
            lines = ff.readlines()
            summary = lines[-1].strip().replace("Feedback:", "").strip()
    except:
        summary = "No feedback"

    return [uid, timestamp, score, summary]


def export_scores():
    logs = glob.glob(os.path.join(RESULTS_DIR, "*_output.log"))
    records = []

    for log_path in logs:
        uid = os.path.basename(log_path).split("_")[0]
        score_path = os.path.join(RESULTS_DIR, f"{uid}.score")
        feedback_path = os.path.join(RESULTS_DIR, f"{uid}.feedback")

        if os.path.exists(score_path) and os.path.exists(feedback_path):
            records.append(extract_metadata(log_path, score_path, feedback_path))

    if records:
        with open(CSV_PATH, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["UID", "Timestamp", "Score", "Feedback Summary"])
            writer.writerows(records)

        print(f"[📁] Score data exported to: {CSV_PATH}")
    else:
        print("[⚠️] No complete results to export.")


if __name__ == "__main__":
    export_scores()