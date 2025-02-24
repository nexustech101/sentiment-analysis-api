# ./routers/routes.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import SentimentRequest, SentimentResponse
from models.sentiment import get_sentiment_analysis

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/sentiment", response_model=List[SentimentResponse])
async def analyze_sentiment(request: SentimentRequest):
    try:
        return Response(get_sentiment_analysis(request.prompts))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
