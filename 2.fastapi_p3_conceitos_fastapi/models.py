"""
IMPORTAÇÕES
from typing import Optional: Importa a classe Optional do módulo typing. 
Optional é usado para indicar que um campo pode ter um valor ou ser None (nulo).

from pydantic import BaseModel: Importa a classe BaseModel da biblioteca pydantic. 
BaseModel é a classe base que você usa para definir modelos de dados com pydantic

pydantic BASEMODEL
class Curso(BaseModel): Define uma classe chamada Curso que herda de BaseModel.
Isso significa que a classe Curso usará as funcionalidades e validações fornecidas pelo
pydantic.

Em resumo:

Este código define um modelo de dados chamado Curso que representa um curso. O modelo define os seguintes campos:

id: Um identificador opcional do curso (pode ser um inteiro ou None).
titulo: O título do curso (uma string).
aulas: O número de aulas do curso (um inteiro).
horas: A duração do curso em horas (um inteiro)

Como isso é útil?

Validação de dados: pydantic valida automaticamente os dados que você passa para criar um objeto Curso. Por exemplo, se você tentar criar um Curso com um titulo que não seja uma string ou com aulas que não seja um inteiro, pydantic irá gerar um erro.
Conversão de dados: pydantic pode converter automaticamente dados de diferentes formatos (como JSON) para o tipo de dados correto definido no modelo.
Documentação automática: pydantic pode gerar automaticamente documentação para seus modelos, o que é muito útil para APIs.
"""


from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

