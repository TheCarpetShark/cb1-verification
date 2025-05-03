def generate_code(task):
    prompt = f"Write a Python script to: {task}"
    result = run(["gpt4all", "--prompt", prompt], capture_output=True, text=True)
    code = result.stdout.strip()

    if not code:
        print("[⚠️] GPT4All returned empty code.")
        return "# Error: No code generated.\n"

    return code
