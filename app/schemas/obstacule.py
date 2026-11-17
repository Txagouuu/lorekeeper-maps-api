from base import BaseEntity

class Obstacule(BaseEntity):
    blocks_movement: bool = True
    blocks_vision: bool = True
