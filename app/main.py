from uuid import UUID
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.core.core import get_session_db
from app.db.models import MapDB
from app.schemas.map import MapState
from app.schemas.actions import Action
from app.websockets.manager import ConnectionManager
from app.routers import maps, ws
app = FastAPI(title="Lorekeeper Maps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Em produção, troque pela URL do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(maps.router)
app.include_router(ws.router)