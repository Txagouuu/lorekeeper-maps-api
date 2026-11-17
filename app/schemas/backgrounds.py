from pydantic import BaseModel

class GoblalBackgound(BaseModel):

    asset_id: str
    scale: float = 1.0
    offset_x: int = 0
    offeset_y: int = 0


class BackgroundTile(BaseModel):

    x_pos: int
    y_pos: int
    asset_id: str
    rotation:int = 0