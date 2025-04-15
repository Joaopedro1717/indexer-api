from pydantic import BaseModel
from typing import Optional

class TattoArtistBase(BaseModel):
    name: str
    username: str
    description: Optional[str] = ""
    hashtags: Optional[str] = ""

class TattoArtistCreate(TattoArtistBase):
    pass

class TattoArtistRead(TattoArtistBase):
    id: int
