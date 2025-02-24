    
# ./routers/sentiment_route.py

import json
from typing import List
from functools import lru_cache
from fastapi import FastAPI, HTTPException, APIRouter, Response
from utils.sentiment_utils import get_sentiments, load_sentiment_labels
from models.models import SentimentRequest, SentimentResponse

router = APIRouter(
    prefix="/v1/api"
)

# Route gets a sentiment class from json config and returns sentiments data to user
@router.post("/sentiment/{label_group}", response_model=List[SentimentResponse])
@router.post("/sentiment", response_model=List[SentimentResponse])
def analyze_sentiment(request: SentimentRequest, label_group: str = None):
    sentiment_labels = load_sentiment_labels()
    candidate_labels = sentiment_labels.get(label_group) if label_group else sentiment_labels.get("all")
    
    if not candidate_labels:
        raise HTTPException(status_code=400, detail="Invalid label group. Further sentiment customization is underway.")
    try:
        return get_sentiments(candidate_labels, request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
