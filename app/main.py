from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import SessionLocal

from app.services.indexer import index_artist
from app.schemas.tatto_artist import TattoArtistCreate, TattoArtistRead
from app.repositories.tatto_artist_repo import create_tatto_artist
from app.storage.index_storage import inverted_index

app = FastAPI(
    title="Tatto indexer API",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class IndexPayload(BaseModel):
    artist: TattoArtistCreate
    artist_id: int


@app.post("/index")
def index_endpoint(payload: IndexPayload, db: Session = Depends(get_db)):

    db_artist = create_tatto_artist(db, payload.artist)

    index_artist(payload.artist, db_artist.id)

    return {"message": "Artist created and indexed successfully", "artist_id": db_artist.id}


@app.post("/artists/", response_model=TattoArtistRead)
def create_and_index_artist(
    artist: TattoArtistCreate,
    db: Session = Depends(get_db)
):
    # Salvar no banco
    db_artist = create_tatto_artist(db, artist)

    # Indexar automaticamente
    index_artist(artist, db_artist.id)

    return db_artist
