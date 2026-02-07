from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    event = request.headers.get("X-GitHub-Event")

    print("EVENT TYPE:", event)

    if event == "pull_request":
        action = payload.get("action")
        pr = payload.get("pull_request", {})
        title = pr.get("title")
        author = pr.get("user", {}).get("login")

        print("PR ACTION:", action)
        print("PR TITLE:", title)
        print("AUTHOR:", author)

    return {"status": "ok"}
