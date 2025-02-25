# ./routers/sentiment_route.py
import json
from typing import List
from functools import lru_cache
from fastapi import FastAPI, HTTPException, APIRouter, Response, Depends
from utils.sentiment_utils import get_sentiments, load_sentiment_labels
from models.models import SentimentRequest, SentimentResponse
from utils.logger import log_info, log_error, log_debug
from utils.rate_limiter import RateLimiter

rate_limiter = RateLimiter(calls=100, period=1)  # 100 requests per day

router = APIRouter(
    prefix="/v1/api"
)

# Route gets a sentiment class from json config and returns sentiments data to user
# Two routes to handle edge case where user forgets to include label_group url param
@router.post("/sentiment/{label_group}", response_model=List[SentimentResponse], dependencies=[Depends(rate_limiter)])
@router.post("/sentiment", response_model=List[SentimentResponse], dependencies=[Depends(rate_limiter)])
async def analyze_sentiment(request: SentimentRequest, label_group: str = None):
    sentiment_labels = load_sentiment_labels()
    candidate_labels = sentiment_labels.get(label_group) if label_group else sentiment_labels.get("all")
    
    if not candidate_labels:
        log_debug(f"Failed to parse candidate_labels: {label_group}")
        raise HTTPException(status_code=400, detail="Invalid label group. Further sentiment customization is underway.")
    try:
        log_info(f"Sentiment analysis requested for text: {request.prompts}")
        return get_sentiments(candidate_labels, request.prompts)
    except ValueError as e:
        log_error(f"Failed to analyze sentiment: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")