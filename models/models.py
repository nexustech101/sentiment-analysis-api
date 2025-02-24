# ./models/models.py

from pydantic import BaseModel
from typing import List, Dict

# Base model to be inherited by al other sentiment models
class Base(BaseModel):
    __info__: str = "Inherits from SentimentRequest parent (Base) model"


# Full sentiment analysis models (abstracts away models for comprehensive documentation and api usage)
class SentimentRequest(Base):
    prompts: List[str]


class SentimentResult(Base):
    label: str
    score: float


class SentimentResponse(Base):
    sequence: str
    sentiments: List[SentimentResult]
