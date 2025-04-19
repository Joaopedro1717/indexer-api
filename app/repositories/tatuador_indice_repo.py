from sqlalchemy.orm import Session
from sqlalchemy import text

def adicionar_token(db: Session, token: str, tatuador_id: int):
    # Verifica se o token já existe
    resultado = db.execute(
        text("SELECT tatuadores_ids FROM TatuadorIndice WHERE token = :token"),
        {"token": token}
    ).fetchone()

    if resultado:
        ids = resultado[0]
        if tatuador_id not in ids:
            ids.append(tatuador_id)
            db.execute(
                text("UPDATE TatuadorIndice SET tatuadores_ids = :ids WHERE token = :token"),
                {"ids": ids, "token": token}
            )
    else:
        db.execute(
            text("INSERT INTO TatuadorIndice (token, tatuadores_ids) VALUES (:token, :ids)"),
            {"token": token, "ids": [tatuador_id]}
        )
    db.commit()