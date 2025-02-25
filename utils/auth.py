# utils/auth.py
import os
import jwt
import sqlite3
from dotenv import load_dotenv
from fastapi import HTTPException, Depends, Request
from datetime import datetime, timedelta

# Load envirnemt variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM  = os.getenv("ALGORITHM")


# Simple SQLite connection
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create a user session and generate a JWT token
def create_session(user_id: int):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Verify the token and get user
def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        payload = jwt.decode(token.split("Bearer ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Session expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

# Decorator to protect routes
def require_auth(func):
    async def wrapper(*args, request: Request, **kwargs):
        user = get_current_user(request)
        return await func(*args, user=user, **kwargs)
    return wrapper
