# ./models/models.py

from pydantic import BaseModel
from typing import List, Dict

# Base model to be inherited by al other sentiment models
class Base(BaseModel):  # Excluded for now
    __info__: str = "Inherits from SentimentRequest parent (Base) model"


# Full sentiment analysis models (abstracts away models for comprehensive documentation and api usage)
class SentimentRequest(BaseModel):
    prompts: List[str]


class SentimentResult(BaseModel):
    label: str
    score: float


class SentimentResponse(BaseModel):
    sequence: str
    sentiments: List[SentimentResult]
