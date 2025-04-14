from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.tatto_artist import TattoArtistCreate, TattoArtistRead
from app.repositories.tatto_artist_repo import create_tatto_artist, get_all_artists
from app.core.database import SessionLocal
from app.services.indexer import index_artist

router = APIRouter(prefix="/artist", tags=["Tatto Artists"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TattoArtistRead)
def create_artist(artist: TattoArtistCreate, db: Session = Depends(get_db)):
    db_artist = create_tatto_artist(db, artist)
    index_artist(artist, db_artist.id)
    return db_artist