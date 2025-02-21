from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/webhook")
async def webhook(payload: dict):
    """Triggered when code is pushed to Git"""
    print("Received webhook event:", payload)
    subprocess.run(["git", "pull"])  # Pull latest code

    # Run test
    test_result = subprocess.run(["pytest", "test_helloworld.py"], capture_output=True, text=True)

    if test_result.returncode != 0:
        return {"status": "failed", "error": test_result.stderr}

    return {"status": "success"}
