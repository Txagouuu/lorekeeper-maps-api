from fastapi import APIRouter, Depends,HTTPException,status
from uuid import UUID
from app.core.core import get_session_db
from app.db.models import MapDB
from app.schemas.map import MapState
from app.websockets.manager import manager
from sqlalchemy.orm import Session

router = APIRouter(prefix="/maps",tags=["Maps"])


@router.post("",response_model=MapState,status_code=status.HTTP_201_CREATED)
def create_map(map_data:MapState,db:Session = Depends(get_session_db)):
    db_map = MapDB(id=str(map_data.map_id),state_data=map_data.model_dump(mode="json"))
    
    db.add(db_map)
    db.commit()
    return map_data

@router.get("/{map_id}",response_model=MapState)
def get_map(map_id:UUID,db:Session = Depends(get_session_db)):
    
    if map_id in manager.map_states:
        return manager.map_states[map_id]

    db_map = db.query(MapDB).filter(MapDB.id == str(map_id)).first()
    if not db_map:
        raise HTTPException(status_code=404, detail="Mapa não encontrado")

    map_state = MapState.model_validate(db_map.state_data)
    manager.map_states[map_id] = map_state
    return map_state