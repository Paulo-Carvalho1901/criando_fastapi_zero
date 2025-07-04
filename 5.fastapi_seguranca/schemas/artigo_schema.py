from typing import Optional

from pydantic import BaseModel, HttpUrl


class ArtigoShema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Config:
        from_attributes = True
        