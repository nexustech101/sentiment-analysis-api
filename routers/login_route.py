# ./routers/sentiment_route.py
import json
from typing import List
from functools import lru_cache
from fastapi import FastAPI, HTTPException, APIRouter
from models.user import UserResponse, UserLogin, Token
from passlib.context import CryptContext

router = APIRouter(
    prefix="/v1/login"
)

@router.post("/token", response_model=Token)
def login(user: UserLogin):
    conn = get_db_connection()
    db_user = conn.execute("SELECT * FROM users WHERE username = ?", (user.username,)).fetchone()
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_session(db_user["id"])
    return {"access_token": token, "token_type": "bearer"}