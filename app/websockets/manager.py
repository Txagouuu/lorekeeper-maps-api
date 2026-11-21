from fastapi import WebSocket
from uuid import UUID
from typing import Dict,List
from app.schemas.map import MapState
from app.schemas.actions import Action
from app.schemas.tokens import CharacterToken
from app.schemas.backgrounds import BackgroundTile
from app.schemas.obstacules import Obstacule
class ConnectionManager():
    def __init__(self):
        # active_connections: É um dicionário onde a chave é o map_id e o valor é uma lista com as conexões abertas daquela sala.
        self.active_connections: Dict[UUID,List[WebSocket]] = {}

        # map_states: Guarda o estado atual de cada mapa em RAM durante a sessão (para não ter que ir no SQLite a cada passo de um token).
        self.map_states: Dict[UUID, MapState] = {}

    async def connect(self,websocket:WebSocket,map_id:UUID):
        await websocket.accept()
        if map_id not in self.active_connections:
            self.active_connections[map_id] = []
        self.active_connections[map_id].append(websocket)

    def disconnect(self,websocket:WebSocket,map_id:UUID):
        if map_id in self.active_connections:
            if websocket in self.active_connections[map_id]:
                self.active_connections[map_id].remove(websocket)
            if not self.active_connections[map_id]:
                del self.active_connections[map_id]

    def apply_action(self,map_id:UUID,action:Action) -> bool:
        """
        
        Aplica a Alteração na Memoria do MapState
        Retorna True ou False para caso houver alteração ou não
        
        """
        map_state = self.map_states.get(map_id)
        if not map_state:
            return False

        if action.action_type == "move_token":
            for token in map_state.layers.tokens:
                if token.id == action.target_id:
                    token.x_pos = action.payload["x_pos"]
                    token.y_pos = action.payload["y_pos"]
                    return True
            return False

        elif action.action_type == "add_entity":
            entity_type =   action.payload.get("entity_type")
            data = action.payload.get("data",{})
            if entity_type == "token":
                map_state.layers.tokens.append(CharacterToken.model_validate(data))
                return True
            if entity_type == "obstacule":
                map_state.layers.obstacules.append(Obstacule.model_validate(data))
                return True
            if entity_type == "backgournd_tile":
                map_state.layers.background.append(BackgroundTile.model_validate(data))
                return True
            return False

        elif action.action_type == "remove_token":
            for layer in (map_state.layers.tokens,map_state.layers.obstacles,map_state.layers.background_tiles,):
                for index,entity in enumerate(layer):
                    if entity.id == action.target_id:
                        layer.pop(index)
                        return True
                return False
            return False
        return False
    
    async def broadcast_action(self,map_id:UUID,action:Action):
        if map_id not in self.active_connections:
            return
        action_json = action.model_dump_json()
        dead_connection = []

        for connection in self.active_connections[map_id]:
            try:
                await connection.send_text(action_json)
            except Exception:
                dead_connection.append(connection)

        for dead_ws in dead_connection:

            self.disconnect(dead_ws,map_id)

# Instância global: guarda as salas e os mapas ativos na RAM
manager = ConnectionManager()