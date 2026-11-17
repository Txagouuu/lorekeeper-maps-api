from pydantic import BaseModel,Field
from typing import List
from backgrounds import BackgroundTile
from obstacules import Obstacule
from tokens import CharacterToken



class MapLayers(BaseModel):
    background: List[BackgroundTile] = Field(default_factory=list)
    obstacule: List[Obstacule] = Field(default_factory=list)
    tokens: List[CharacterToken] = Field(default_factory=list)

class MapState(BaseModel):
    map_id: str
    canvas_width: int = 50
    canvas_height: int = 50
    grid_size:int = 50
    layers: MapLayers = Field(default_factory=MapLayers)