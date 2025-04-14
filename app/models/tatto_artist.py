from sqlalchemy import Column, Integer, String
from app.core.database import Base

class TattoArtist(Base):
    __tablename__ = "tatto_artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    description = Column(String)
    hashtags = Column(String)