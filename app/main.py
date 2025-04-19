from fastapi import FastAPI
from api import tatuador
from core.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tatuador.router)