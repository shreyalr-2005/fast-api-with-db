from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from routes.user_routes import router as user_router
from routes.ai_response_routes import router as ai_response_router
from routes.ai_response_routes import router as ai_router
from routes.email_routes import router as email_router
from db import get_db,DATABASE_URL
from sqlalchemy import create_engine
import os
from models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

app.include_router(user_router)
app.include_router(ai_response_router)
app.include_router(email_router)
app.include_router(ai_router,prefix="/ai")
#to create database

engine=create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)