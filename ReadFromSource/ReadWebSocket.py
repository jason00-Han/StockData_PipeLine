from fastapi import FastAPI, WebSocket, Request
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/client")
async def client(request: Request):
    # /templates/client.html파일을 response함
    return templates.TemplateResponse("client.html", {"request":request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")


