from app.schemas.tatto_artist import TattoArtistCreate, TattoArtistRead
from app.services.index_storage import inverted_index

import re

def tokenize(text: str):
    return re.findall(r"\b\w+\b", text.lower())

def index_artist(artist: TattoArtistCreate, artist_id: int):
    fields = [
        artist.name, 
        artist.username,
        artist.description or "",
        artist.hashtags or "",
    ]

    for field in fields: 
        for word in tokenize(field):
            inverted_index[word].add(artist_id)