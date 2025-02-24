# ./routers/emotion_sentiment.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List
from models.models import EmotionSentimentRequest, EmotionSentimentResponse
from models.sentiments import get_emotion_sentiments

router = APIRouter(
    prefix="/v1/api"
)

@router.post("/emotion_sentiment", response_model=List[EmotionSentimentResponse])
def analyze_emotion_sentiment(request: EmotionSentimentRequest):
    try:
        return get_emotion_sentiments(request.prompts)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")