from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.workspaces.router import workspaces_router
from src.auth.router import auth_router

app = FastAPI()

app.include_router(workspaces_router, prefix='')
app.include_router(auth_router, prefix='/auth')

@app.exception_handler(Exception)
async def base_exception_handler(request, exc):
    return JSONResponse({'bad': True})