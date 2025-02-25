# ./utils/rate_limiter.py
from time import time
from collections import deque
from fastapi import HTTPException

class RateLimiter:
    def __init__(self, calls: int, period: int):
        self.allowed_calls = calls
        self.period = period * 86400  # Converts days to seconds
        self.timestamps = []

    def __call__(self):
        current_time = time()
        self.timestamps = [t for t in self.timestamps if t > current_time - self.period]
        if len(self.timestamps) >= self.allowed_calls:
            raise HTTPException(status_code=429, detail="Daily request limit exceeded")
        self.timestamps.append(current_time)
        return True