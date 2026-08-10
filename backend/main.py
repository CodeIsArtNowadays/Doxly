from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.auth.router import auth_router
from src.chat.router import chat_router, ws_router
from src.core.exceptions import ProjectBaseException
from src.docs.router import docs_router
from src.workspaces.router import workspaces_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://139.100.235.44:5174", 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workspaces_router)
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router)
app.include_router(docs_router)
app.include_router(ws_router)

@app.exception_handler(ProjectBaseException)
async def base_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
