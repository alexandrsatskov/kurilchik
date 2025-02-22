from fastapi import FastAPI

app = FastAPI()


@app.get("/token_info")
async def token_info():
    """
    - Информация о токене по адресу (название, символ, общее предложение)
    """
    return {"Hello": "World"}


@app.get("/top_100_holders")
async def top_100_holders():
    """
    - Список топ-100 держателей токена по адресу
    """
    return {"Hello": "World"}


@app.get("/last_50_transactions")
async def last_50_transactions():
    """
    - Последние 50 транзакций для адреса
    """
    return {"Hello": "World"}


@app.get("/follow_address")
async def follow_address():
    """
    - Добавить адрес в список отслеживаемых
    """
    return {"Hello": "World"}


@app.get("/rm_address")
async def rm_address():
    """
    - Удалить адрес из отслеживаемых
    """
    return {"Hello": "World"}
