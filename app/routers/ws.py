from fastapi import APIRouter, Depends, WebSocket,WebSocketDisconnect
from pydantic import ValidationError
from app.schemas.actions import Action
from app.websockets.manager import manager
from uuid import UUID

router = APIRouter(tags=["WebSockets"])

@router.websocket("/ws/{map_id}")
async def websocket_endpoint(websocket:WebSocket,map_id:UUID):
    await manager.connect(websocket,map_id)
    try:
        while True:
            data = await websocket.receive_text()
            try:
                action = Action.model_validate_json(data)
                applied = manager.apply_action( map_id,action)
                if applied:
                    await manager.broadcast_action(map_id,action)
                else:
                    await websocket.send_json({"ERRO":"Mapa ou entidade não encontrada"})
            except ValidationError as e:
                await websocket.send_json({"error":"Ação Invalida","details":e.errors()})

    except WebSocketDisconnect:
        manager.disconnect(websocket,map_id)
        