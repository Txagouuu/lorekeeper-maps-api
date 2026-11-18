from pydantic import BaseModel, Field
from typing import Any,Literal,Dict

class Action(BaseModel):

    action_type:Literal["move_token","remove_entity","add_entity"] = Field(...,description="Ação exercida pelo token")
    target_id:str = Field(...,description="ID que sofre a ação")

    payload:Dict[str,Any] = Field(default_factory=dict)