# evaluator.py
def validate_code(code):
    # Basic test: does it run without crashing?
    try:
        exec(code, {})
        return True
    except Exception as e:
        print(f"[!] Validation failed: {e}")
        return False
