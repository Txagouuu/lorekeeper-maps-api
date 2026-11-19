from pydantic import BaseModel, Field
from typing import Any,Literal,Dict
from uuid import UUID, uuid4
class Action(BaseModel):

    action_type:Literal["move_token","remove_entity","add_entity"] = Field(...,description="Ação exercida pelo token")
    target_id:UUID = Field(default_factory=uuid4,description="ID que sofre a ação")

    payload:Dict[str,Any] = Field(default_factory=dict)