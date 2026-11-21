from fastapi import APIRouter, Depends,HTTPException,status
from uuid import UUID
from app.core.core import get_session_db
from app.db.models import MapDB
from app.schemas.map import MapState
from app.websockets.manager import manager
from sqlalchemy.orm import Session

router = APIRouter(prefix="/maps",tags=["Maps"])


router.post("",response_model=MapState,status_code=status.HTTP_201_CREATED)
def create_map(map_data:MapDB,db:Session = Depends(get_session_db)):
    db_map = MapDB(id=str(map_data.id),state_data=map_data.model_dump(mode="json"))
    
    db.add(db_map)
    db.commit()
    return map_data

