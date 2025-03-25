from fastapi import FastAPI, WebSocket, Request
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

KAFKA_BROKER = "localhost:29092"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")


