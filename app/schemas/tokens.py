from typing import Optional
from base import BaseEntity


class CharacterBase(BaseEntity):
    
    name:str
    type:str
    size:int = 1
    hp_current: Optional[int] = None

