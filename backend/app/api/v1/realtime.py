from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

connections: list[WebSocket] = []

async def broadcast(message: str):
    for ws in list(connections):
        try:
            await ws.send_text(message)
        except Exception:
            connections.remove(ws)

@router.websocket("/ws/status")
async def websocket_status(ws: WebSocket):
    await ws.accept()
    connections.append(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        connections.remove(ws)
