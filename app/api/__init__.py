from fastapi import APIRouter
from app.api import tatto_artist, search

router = APIRouter()
router.include_router(tatto_artist.router)
router.include_router(search.router)