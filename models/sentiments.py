# ./models/models.py
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

# Base model to be inherited by al other sentiment models
class Base(BaseModel):  # Excluded for now
    __info__: str = "Inherits from SentimentRequest parent (Base) model"

class SentimentRequest(BaseModel):
    prompts: List[str]

class SentimentResult(BaseModel):
    label: str
    confidence: float


# User models for api validation and session tokenization
class SentimentResponse(BaseModel):
    sequence: str
    sentiments: List[SentimentResult]
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"