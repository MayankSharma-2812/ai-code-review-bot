from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "server alive"}

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    print("Webhook received")
    print(payload.get("action"))
    return {"ok": True}
