# score_tracker.py
import os
import glob
import statistics

RESULTS_DIR = "./sandbox_results"

def load_scores():
    scores = []
    for file in glob.glob(os.path.join(RESULTS_DIR, "*.score")):
        with open(file, "r") as f:
            try:
                score = int(f.read().strip())
                scores.append(score)
            except ValueError:
                continue
    return scores

def summarize_scores():
    scores = load_scores()
    total = len(scores)
    passed = sum(1 for s in scores if s >= 100)
    failed = total - passed

    print("\n===== SCORE SUMMARY =====")
    print(f"Total runs:   {total}")
    print(f"Passed:       {passed}")
    print(f"Failed:       {failed}")

    if total > 0:
        print(f"Pass rate:    {passed / total:.2%}")
        print(f"Average score:{statistics.mean(scores):.2f}")
        print(f"Min score:    {min(scores)}")
        print(f"Max score:    {max(scores)}")
    else:
        print("No scores found.")

if __name__ == "__main__":
    summarize_scores()