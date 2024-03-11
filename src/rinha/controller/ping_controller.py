from rinha.settings import app

@app.get("/")
async def ping():
    return {"pong": True}