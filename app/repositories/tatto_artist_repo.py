from sqlalchemy.orm import Session
from app.models.tatto_artist import TattoArtist
from app.schemas.tatto_artist import TattoArtistCreate, TattoArtistRead

def create_tatto_artist(db: Session, artist: TattoArtistCreate):
    db_artist = TattoArtist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_all_artists(db: Session):
    return db.query(TattoArtist).all()