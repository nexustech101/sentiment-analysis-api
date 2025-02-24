# ./routers/speach_sentiment.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import SpeachSentimentRequest, SpeachSentimentResponse
from models.sentiment import get_speach_sentiments

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/speach_sentiment", response_model=List[SpeachSentimentResponse])
def analyze_speach_sentiment(request: SpeachSentimentRequest):
    try:
        return get_speach_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")