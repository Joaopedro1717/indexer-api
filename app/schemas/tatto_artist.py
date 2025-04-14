from pydantic import BaseModel

class TattoArtistBase(BaseModel):
    name: str
    username: str
    description: str | None = None
    hashtags: str | None = None

class TattoArtistCreate(TattoArtistBase):
    pass

class TattoArtistRead(TattoArtistBase):
    id: int

    class Config:
        orm_mode = True