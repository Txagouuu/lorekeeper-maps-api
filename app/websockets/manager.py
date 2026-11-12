from fastapi import FastAPI,WebSocketDisconnect,WebSocket


websocket = FastAPI(title="")


@websocket.websocket("/ws/maps/{map_id}")
async def maps_endpoint(websocket:WebSocket, map_id:int):
    await websocket.accept()
    print(f"Nova conexão no mapa:{map_id}")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Mensagem RECEBIDA: {data}")

            await websocket.send_text(f"Pacote recebido pelo BACKEND {data} ")
    except WebSocketDisconnect:
        print(f"Cliente desconectou do mapa {map_id}")