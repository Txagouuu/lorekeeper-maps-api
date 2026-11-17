import uuid
from pydantic import BaseModel,Field

class BaseEntity(BaseModel):
    id: str = Field(default_factory=lambda:str(uuid.uuid4()),description="Identificador unico da entidade")
    x_pos:int = Field(...,ge=0,description="Coordenada X")
    y_pos:int = Field(..., ge=0,description="Coordenada Y")
    asset_id:str = Field(...,description="ID curto da imagem no frontend")
