from fastapi import APIRouter
from app.services.index_storage import inverted_index

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(term: str):
    words = term.lower().split()
    results = [inverted_index.get(word, set()) for word in words]
    if results:
        # Retorna interseção (AND entre termos)
        matching_ids = list(set.intersection(*results))
    else:
        matching_ids = []
    return {"matching_ids": matching_ids}