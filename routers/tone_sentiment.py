# ./routers/tone_sentiment.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import ToneSentimentRequest, ToneSentimentResponse
from models.sentiments import get_tone_sentiments

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/tone_sentiment", response_model=List[ToneSentimentResponse])
def analyze_tone_sentiment(request: ToneSentimentRequest):
    try:
        return get_tone_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")