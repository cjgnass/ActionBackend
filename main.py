from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello!"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except Exception:
        await websocket.close()
