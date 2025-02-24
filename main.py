# ./main.py (API entry point)
import uvicorn
from fastapi import FastAPI, HTTPException
from routers.sentiment_route import router as sentiment_route

# Init FastAPI module
app = FastAPI()

# Register routes with main app router
app.include_router(sentiment_route)
