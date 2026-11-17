from pydantic import Field
from .base import BaseEntity

class Obstacule(BaseEntity):
    blocks_movement: bool = Field(default=True,description="se verdadeiro,tokens nao podem entrar nesta coordenada") 
    blocks_vision: bool = Field(default=True,description="Se verdadeiro, projeta sombra/bloqueio a visao do jogador")

