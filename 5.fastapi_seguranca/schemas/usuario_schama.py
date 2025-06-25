from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoShema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        from_attributes = True
        

class UsuarioShemaCreate(UsuarioSchemaBase):
    senha: str


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoShema]]


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
