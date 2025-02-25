# ./main.py (API entry point)
import uvicorn
from fastapi import FastAPI, HTTPException
from routers.sentiment_route import router as sentiment_route
from utils.logger import log_requests

# Init FastAPI module
app = FastAPI()

# Middleware for logging traffic and errors
app.middleware("http")(log_requests)

# Register routes with main app router
app.include_router(sentiment_route)
