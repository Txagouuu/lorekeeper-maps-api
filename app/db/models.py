from sqlalchemy import Column,String,JSON,create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.core import Base

class MapDB(Base):
    __tablename__ = "maps"
    id = Column(String,primary_key=True,index=True)
    state_data = Column(JSON,nullable=False)