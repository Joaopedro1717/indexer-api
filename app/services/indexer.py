from app.schemas.tatto_artist import TattoArtistCreate, TattoArtistRead
from app.storage.index_storage import inverted_index

import re

def tokenize(text: str):
    return re.findall(r"\b\w+\b", text.lower())

def index_artist(artist: TattoArtistCreate, artist_id: int):
    field_map = {
        "name": artist.name,
        "username": artist.username,
        "description": artist.description or "",
        "hashtags": artist.hashtags or "",
    }

    for field , value in field_map.items(): 
        for word in tokenize(value):
            inverted_index[word].add(artist_id) #busca genérica
            inverted_index[f"{field}:{word}"].add(artist_id) #busca por campo

    print(f"Indexado artista: {artist.name} com ID: {artist_id}")
    print("Índice atual:")
    for k, v in inverted_index.items():
        print(f"{k}: {v}")