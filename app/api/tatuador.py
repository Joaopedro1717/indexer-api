import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from schemas.tatuador import TatuadorCreate
from repositories.tatuador_repo import create_tatuador
from repositories import tatuador_indice_repo

router = APIRouter()

TOKENIZER_URL = "http://localhost:8001/tokenize" 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tatuador")
def criar_tatuador(tatuador: TatuadorCreate, db: Session = Depends(get_db)):
    #Cria o tatuador 
    novo_tatuador = create_tatuador(db, tatuador)

    #Junta os dados em uma frase só
    frase = " ".join ([
        tatuador.nome_de_usuario,
        tatuador.nome_completo,
        tatuador.descricao,
        " ".join(tatuador.hashtags)
    ]) 

    #Envia ao serviço tokenizador
    try:
        response = requests.post(TOKENIZER_URL, json={"text": frase})
        response.raise_for_status()
        tokens = response.json()
    except requests.RequestException as e:
        print("Erro ao se comunicar com o serviço de tokenização:", e)
        tokens = []

    #Salva os dodos no banco
    for token in set(tokens):
        tatuador_indice_repo.adicionar_token(db, token, novo_tatuador.id)    
    
    return novo_tatuador
