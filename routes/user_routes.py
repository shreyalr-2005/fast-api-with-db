from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from repositories.user_repo import userRepo
router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "User signed up successfully"}

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}
