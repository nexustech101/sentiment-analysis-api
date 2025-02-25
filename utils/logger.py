# ./utils/logger.py
import logging
from logging.handlers import RotatingFileHandler
from fastapi import Request

# Configure logger
logger = logging.getLogger("sentiment-analysis")
logger.setLevel(logging.DEBUG)

# File handler for rotating logs
file_handler = RotatingFileHandler("logs/server.log", maxBytes=5_000_000, backupCount=5)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Stream handler for console output in development
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Middleware for request logging
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


# Function to log errors
def log_error(message: str):
    logger.error(message)


# Function to log warnings
def log_warning(message: str):
    logger.warning(message)


# Function to log debug information
def log_debug(message: str):
    logger.debug(message)


# Function to log info
def log_info(message: str):
    logger.info(message)
