# ./routers/profession_sentiment.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import SentimentRequest, SentimentResponse
from models.sentiments import get_profession_sentiments

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/profession_sentiment", response_model=List[SentimentResponse])
def analyze_profession_sentiment(request: SentimentRequest):
    try:
        return get_profession_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")