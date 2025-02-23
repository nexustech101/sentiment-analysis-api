# ./models/models.py

from pydantic import BaseModel
from typing import List, Dict


class SentimentRequest(BaseModel):
    prompts: List[str]


class SentimentResult(BaseModel):
    label: str
    score: float


class SentimentResponse(BaseModel):
    sequence: str
    sentiments: List[SentimentResult]


class SentimentJSON(BaseModel):
    results: List[SentimentResponse]
