# ./utils/rate_limiter.py
from time import time
from functools import wraps
from collections import deque
from fastapi import HTTPException, Request

# Classes can maintain state, such as the number of requests made within a time window, more effectively.
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

# Decorators offer a concise way to apply rate limiting to individual route functions.
def rate_limiter(calls: int, period: float):
    period *= 86400  # Converts days to seconds
    timestamps = []

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_time = time()
            nonlocal timestamps
            timestamps = [t for t in timestamps if t > current_time - period]
            if len(timestamps) >= calls:
                raise HTTPException(status_code=429, detail="Daily request limit exceeded.")
            timestamps.append(current_time)
            return await func(*args, **kwargs)
        return wrapper

    return decorator
