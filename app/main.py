from fastapi import FastAPI
from app.core.config import settings 
from app.db.session import engine

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health_check():
    return {
         "status: ": "ok",
         "env": settings.env
            
            }

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        return {
            "db" : "connected"
        }

