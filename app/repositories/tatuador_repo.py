from sqlalchemy.orm import Session
from models.tatuador import Tatuador, Hashtag, TatuadorHashtag
from schemas.tatuador import TatuadorCreate

def create_tatuador(db: Session, tatuador_data: TatuadorCreate):
    #Criar tatuador
    novo_tatuador = Tatuador(
        nome_de_usuario=tatuador_data.nome_de_usuario,
        nome_de_exibicao=tatuador_data.nome_completo,
        descricao=tatuador_data.descricao
    )
    db.add(novo_tatuador)
    db.commit()
    db.refresh(novo_tatuador)

    #Verificar/Criar Hashtags
    for tag in tatuador_data.hashtags:
        hashtag = db.query(Hashtag).filter(Hashtag.hashtag == tag).first()
        if not hashtag:
            hashtag = Hashtag(hashtag=tag)
            db.add(hashtag)
            db.commit()
            db.refresh(hashtag)

        #Criar relacionamento entre tatuador e hashtag
        assoc = TatuadorHashtag(tatuador_id=novo_tatuador.id, hashtag_id=hashtag.id)
        db.add(assoc)
    
    db.commit()
    return novo_tatuador
