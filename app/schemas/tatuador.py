from pydantic import BaseModel
from typing import List

class TatuadorCreate(BaseModel):
    nome_de_usuario: str
    nome_completo: str
    descricao: str
    hashtags: List[str]
    
