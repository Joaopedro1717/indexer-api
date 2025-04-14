from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from sqlalchemy import text
from app.api import router as api_router
from app.core.database import Base, engine
from app.models import tatto_artist

app = FastAPI(
    title="Tatto indexer API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "Database connection is working!"}
    except Exception as e:
        return {"error": str(e)}
    

app.include_router(api_router)