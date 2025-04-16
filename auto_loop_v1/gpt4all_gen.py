# gpt4all_gen.py
def generate_code(prompt):
    from subprocess import run, PIPE

    cmd = ["python", "local_gpt_query.py", prompt]
    result = run(cmd, capture_output=True, text=True)
    return result.stdout
