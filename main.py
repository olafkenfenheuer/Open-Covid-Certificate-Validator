import uvicorn


async def app(scope, receive, send):
    pass
if __name__ == "__main__":
    uvicorn.run("occv:app", host="0.0.0.0", port=8001, log_level="info")
