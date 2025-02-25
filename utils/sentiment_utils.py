# ./models/sentiment.py
from functools import lru_cache
from transformers import pipeline
from fastapi import HTTPException
from models.models import *
from utils.logger import log_debug, log_info, log_error
from typing import List
import json
import sys

# Caching sentiment labels for models and labels avoids repeated heavy computations — great performance optimization.
@lru_cache(maxsize=1)
def load_sentiment_labels():
    try:
        log_info("Loading sentiment labels from file...")
        with open("sentiment_labels.json") as f:
            labels = json.load(f)
            log_debug(f"Sentiment labels loaded successfully: {labels}")
            return labels
    except FileNotFoundError as e:
        log_error(f"File not found: sentiment_labels.json — {str(e)}")
        raise HTTPException(status_code=500, detail="Sentiment labels configuration file not found")
    except json.JSONDecodeError as e:
        log_error(f"Error decoding JSON from sentiment_labels.json — {str(e)}")
        raise HTTPException(status_code=500, detail="Error decoding sentiment labels configuration file")
    except Exception as e:
        log_critical(f"Unexpected error loading sentiment labels — {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error loading sentiment labels: {str(e)}")


# Caching classifier pipeline for models and labels avoids repeated heavy computations — great performance optimization.
@lru_cache(maxsize=1)
def get_classifier():
    try:
        log_info("Initializing sentiment classifier pipeline...")
        # classifier = pipeline("zero-shot-classification", model="bart-large-mnli") # Needs api key
        classifier = pipeline("zero-shot-classification")
        if not classifier:
            log_critical("Failed to initialize classifier pipeline")
            raise ValueError("Failed to initialize the classifier pipeline")
        log_info("Sentiment classifier initialized successfully")
        return classifier
    except Exception as e:
        log_critical(f"Error initializing classifier — {str(e)}")
        raise RuntimeError(f"Error initializing classifier: {str(e)}")


# Function for retrieving sentiment analysis on data passed in (optional labels parameter in router logic)
def get_sentiments(sentiment_labels: List[str], prompts: List[str]) -> List[SentimentResponse]:
    classifier = get_classifier()  # cache the classifier object instance
    
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=sentiment_labels)
            
            # Create a list of SentimentResult objects
            sentiments = [
                SentimentResult(label=label, confidence=round(confidence, 8))
                for label, confidence in zip(res['labels'], res['scores'])
            ]
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            log_error(f"Error processing prompt '{prompt}': {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    log_info(f"Sentiment analysis completed for {len(results)} prompts")
    return results  # Return list of SentimentResponse objects directly