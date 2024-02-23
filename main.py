
from fastapi import FastAPI

from database import create_tables, delete_tables
from contextlib import asynccontextmanager

from router import router





@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Всё очистил')
    await create_tables()
    print('Базу создал')
    yield
    print('Выключение ')

app = FastAPI(lifespan=lifespan)
 
app.include_router(router)



