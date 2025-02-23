# ./routers/routes.py

from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from transformers import pipeline
from typing import List
from models.models import SentimentRequest, SentimentResponse, SentimentResult
from models.sentiment import get_sentiment_analysis

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/sentiment", response_model=List[SentimentResponse])
async def analyze_sentiment(request: SentimentRequest):
    try:
        return get_sentiment_analysis(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/test")
async def test_route():
    try:
        return { "response": "API is working!" }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")