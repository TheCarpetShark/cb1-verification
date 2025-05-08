# auryn_memory_proxy.py

from fastapi import FastAPI, Request
import uvicorn
import httpx
import datetime

app = FastAPI()
model_url = "http://127.0.0.1:5000/v1/chat/completions"
CTX_LIMIT = 8192
SAFE_MARGIN = 7000
KEEP = 512

# Memory log (will later persist to disk or Redis)
memory_log = []

def count_tokens(messages):
    return sum(len(m.get("content", "").split()) for m in messages)

def summarize_memory(memory):
    return {
        "role": "system",
        "content": f"<<Summary>>\nPrior tokens exceeded {SAFE_MARGIN}. Memory was trimmed here.\n"
    }

@app.post("/v1/chat/completions")
async def proxy_chat(request: Request):
    payload = await request.json()
    messages = payload.get("messages", [])

    n_past = count_tokens(messages)
    print(f"[{datetime.datetime.now()}] Tokens used: {n_past}")

    # Trigger summarization if exceeding safe margin
    if n_past > SAFE_MARGIN:
        messages = messages[-6:]  # Keep only most recent 6 messages
        messages.insert(0, summarize_memory(memory_log))  # Add summary header
        payload["messages"] = messages

    memory_log.extend(messages)

    async with httpx.AsyncClient() as client:
        response = await client.post(model_url, json=payload)
        return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5050)
