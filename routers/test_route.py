# ./routers/test_route.py

from fastapi import FastAPI, HTTPException, APIRouter, Response
from typing import List

router = APIRouter(
    prefix="/v1/api"
)

@router.get("/test")
async def test_route():
    try:
        return {"response": "API is working!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")