# ./main.py

import uvicorn
from routers.routes import router as sentiment_router
from fastapi import FastAPI, HTTPException

app = FastAPI()

app.include_router(sentiment_router)
