from pydantic import Field
from base import BaseEntity


class CharacterToken(BaseEntity):
    
    name:str = Field(...,description="Nome do personagem/monstro")
    type_token:str = Field(...,description="Categorias: 'player', 'enemy', 'npc' ....")
    size:int = Field(default=1,description="Tamanho da entidade no grid 1(1x1)")
    is_down:bool = Field(default=False,description="indica se está consciente")