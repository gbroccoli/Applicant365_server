from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List

app = APIRouter()

class Message(BaseModel):
    author: str
    content: str

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: Message):
        for connection in self.active_connections:
            await connection.send_text(f"{message.author}: {message.content}")

manager = ConnectionManager()

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                json_data = Message.parse_raw(data)
                await manager.broadcast(json_data)
            except ValueError:
                pass
    except WebSocketDisconnect:
        manager.disconnect(websocket)

routers = [app]