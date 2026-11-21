from pydantic import BaseModel,Field
from .base import BaseEntity
from uuid import UUID, uuid4
class GoblalBackgound(BaseModel):

    asset_id: UUID = Field(default_factory=uuid4,min_length=1,description="ID ")
    scale: float = Field(default=1.0,gt=0,description="Esacala do fundo global")
    offset_x: int = Field(default=0,description="Deslocamento horizontal")
    offeset_y: int = Field(default=0,description="Deslocamento vertical")


class BackgroundTile(BaseEntity):

    asset_id: UUID = Field(default_factory=uuid4, min_length=1,description="ID da textura do tile")
    rotation:int = Field(default=0, ge=0, lt=360, description="Rotação do objeto")