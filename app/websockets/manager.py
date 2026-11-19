from fastapi import WebSocket
from typing import Dict,List
from schemas.map import MapState
class ConnectionManager():
    def __init__(self):
        # active_connections: É um dicionário onde a chave é o map_id e o valor é uma lista com as conexões abertas daquela sala.
        self.active_connections: Dict[str,List[WebSocket]] = {}

        # map_states: Guarda o estado atual de cada mapa em RAM durante a sessão (para não ter que ir no SQLite a cada passo de um token).
        self.map_states: Dict[str, MapState] = {}

    async def connect(self,websocket:WebSocket,map_id:str):
        await websocket.accept()
        if map_id not in self.active_connections:
            self.active_connections[map_id] = []
        self.active_connections[map_id].append(websocket)

