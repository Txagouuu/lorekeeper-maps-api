from uuid import UUID,uuid4
from pydantic import BaseModel,Field
from typing import List
from .backgrounds import BackgroundTile
from .obstacules import Obstacule
from .tokens import CharacterToken



class MapLayers(BaseModel):
    background: List[BackgroundTile] = Field(default_factory=list)
    obstacules: List[Obstacule] = Field(default_factory=list)
    tokens: List[CharacterToken] = Field(default_factory=list)

class MapState(BaseModel):
    map_id: UUID = Field(default_factory=uuid4,description="ID do mapa")
    canvas_width: int = Field(default=50,description="Largura do grid")
    canvas_height: int = Field(default=50,description="Altura do grid")
    grid_size:int = Field(default=50, description="Tamanho do mapa")
    layers: MapLayers = Field(default_factory=MapLayers)