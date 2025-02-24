# ./main.py

import uvicorn
from routers.sentiment import router as sentiment_router
from routers.test_route import router as test_router
from fastapi import FastAPI, HTTPException

# Init FastAPI module
app = FastAPI()

# Register routes with main app router
app.include_router(sentiment_router)
app.include_router(test_router)
