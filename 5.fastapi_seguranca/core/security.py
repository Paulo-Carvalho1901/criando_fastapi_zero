from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def varificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correto, comparando
    a senha em texto puro, informado pelo usuário, e o hash da
    senha que estará salvo no banco de dados durante a criação
    da conta.
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera o retorno o hash da senha 
    """
    return CRIPTO.hash(senha)