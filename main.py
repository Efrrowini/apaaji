from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers.chat import router as chat_router

app = FastAPI(title="Apaaji API")

app.include_router(chat_router, prefix="/api")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")