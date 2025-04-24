from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # MAIS DE 12 AULAS
    horas: int # MAIS DE 10 HORAS

    #CRIANDO VALIDAÇÃO NO TITULO
    @validator('titulo')
    def validar_titulo(cls, value):
        # validação 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')
        
        # validação 2
        if value.islower():
            raise ValueError('O título deve ser caítalizado.')

        return value

cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algoritmo e lógica de programação', aulas=52, horas=66),
]

