from core.configs import settings
from core.database import enjine

async def create_table() -> None:
    import models._all_models
    print('Criando as tabelas no banco de dados')

    async with enjine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.creat_all)
    print('Tabelas criadas com sucesso.')


if __name__ == '__main__':
    import asyncio 

    asyncio.run(create_table())