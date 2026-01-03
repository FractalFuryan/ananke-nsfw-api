from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="ananke-nsfw", version="0.1")
app.include_router(router, prefix="/v1")
