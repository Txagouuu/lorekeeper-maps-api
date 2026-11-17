from pydantic import BaseModel

class BaseEntity(BaseModel):
    id: str
    x_pos:int
    y_pos:int
    asset_id:str