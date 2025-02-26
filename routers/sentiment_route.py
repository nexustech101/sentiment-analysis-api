# ./routers/sentiment_route.py
import json
from typing import List
from functools import lru_cache
from fastapi import FastAPI, HTTPException, APIRouter, Response, Depends
from utils.sentiment_utils import get_sentiments, load_sentiment_labels
from models.sentiments import SentimentRequest, SentimentResponse
from utils.logger import log_info, log_error, log_debug
from utils.rate_limiter import RateLimiter, rate_limiter

# rate_limiter = RateLimiter(calls=3, period=1)  # 100 requests per day: class implementation

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/sentiment/{label_group}", response_model=List[SentimentResponse])
@router.post("/sentiment", response_model=List[SentimentResponse])
@rate_limiter(calls=3, period=0.041667)  # 100 requests per day [hours for testing]
async def analyze_sentiment(request: SentimentRequest, label_group: str = None):
    sentiment_labels = load_sentiment_labels()
    candidate_labels = sentiment_labels.get(label_group) if label_group else sentiment_labels.get("all")
    
    if not candidate_labels:
        log_debug(f"User requested invalid sentiment - {label_group}")
        raise HTTPException(status_code=400, detail="Invalid sentiment label.")
    try:
        log_info(f"Sentiment analysis requested for text - {request.prompts}")
        return get_sentiments(candidate_labels, request.prompts)
    except ValueError as e:
        log_error(f"Failed to analyze sentiment: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")