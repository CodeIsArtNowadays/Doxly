from fastapi import FastAPI

from src.api import api_router
from src.auth import auth_router

app = FastAPI()

app.include_router(api_router, prefix='')
app.include_router(auth_router, prefix='/auth')

