# ./routers/emotion_sentiment.py

import json
from functools import lru_cache
from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import SentimentRequest, SentimentResponse
from models.sentiments import get_emotion_sentiments, get_sentiments

router = APIRouter(
    prefix="/v1/api"
)

# Cache sentiment labels loading
@lru_cache(maxsize=1)
def load_sentiment_labels():
    with open("sentiment_labels.json") as f:
        return json.load(f)

@router.post("/emotion_sentiment", response_model=List[SentimentResponse])
def analyze_emotion_sentiment(request: SentimentRequest):
    sentiment_labels = load_sentiment_labels()
    candidate_labels = sentiment_labels.get("emotion")
    
    if not candidate_labels:
        raise HTTPException(status_code=400, detail="Invalid label group")
    try:
        return get_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")