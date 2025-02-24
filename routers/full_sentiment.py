# ./routers/full_sentiment.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import FullSentimentRequest, FullSentimentResponse
from models.sentiments import get_all_sentiments

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/full_sentiment", response_model=List[FullSentimentResponse])
async def analyze_full_sentiment(request: FullSentimentRequest):
    try:
        return get_all_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
