from pydantic import BaseModel

class BaseEntity(BaseModel):
    id: str
    x_pos:int
    y_pos:int
    assert_id:str