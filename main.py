from fastapi import FastAPI

from src.workspaces.router import workspaces_router
from src.auth.router import auth_router

app = FastAPI()

app.include_router(workspaces_router, prefix='')
app.include_router(auth_router, prefix='/auth')

