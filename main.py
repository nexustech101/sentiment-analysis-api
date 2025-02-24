# ./main.py

import uvicorn
from fastapi import FastAPI, HTTPException
from routers.full_sentiment import router as full_sentiment_route
from routers.test_route import router as test_route
from routers.emotion_sentiment import router as emotion_sentiment_route
from routers.tone_sentiment import router as tone_sentiment_route
from routers.speach_sentiment import router as speach_sentiment_route
from routers.profession_sentiment import router as profession_sentiment_route

# Init FastAPI module
app = FastAPI()

# Register routes with main app router
app.include_router(full_sentiment_route)
app.include_router(emotion_sentiment_route)
app.include_router(tone_sentiment_route)
app.include_router(speach_sentiment_route)
app.include_router(profession_sentiment_route)

# Test route to verify module structure and routes is/are working
app.include_router(test_route)
