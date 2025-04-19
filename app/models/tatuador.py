from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.database import Base

class Tatuador(Base):
    __tablename__ = "Tatuador"

    id = Column(Integer, primary_key=True, index=True)
    nome_de_usuario = Column(String(32), nullable=False)
    nome_de_exibicao = Column(String(64), nullable=False)
    descricao = Column(String(256), nullable=False)

    hashtags = relationship("Hashtag", secondary="Tatuador_Hashtag", back_populates="tatuadores")

class Hashtag(Base):
    __tablename__ = "Hashtag"

    id = Column(Integer, primary_key=True, index=True)
    hashtag = Column(String(128), nullable=False, unique=True)

    tatuadores = relationship("Tatuador", secondary="Tatuador_Hashtag", back_populates="hashtags")

class TatuadorHashtag(Base):
    __tablename__ = "Tatuador_Hashtag"
    
    id = Column(Integer, primary_key=True, index=True)
    tatuador_id = Column(Integer, ForeignKey("Tatuador.id"), nullable=False)
    hashtag_id = Column(Integer, ForeignKey("Hashtag.id"), nullable=False)

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from core.database import Base

class TatuadorIndice(Base):
    __tablename__ = "tatuador_indice"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, index=True)
    artist_id = Column(Integer, index=True)  
