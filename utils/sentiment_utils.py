# ./models/sentiment.py
from functools import lru_cache
from transformers import pipeline
from fastapi import HTTPException
from models.models import *
from typing import List
import json
import sys

# Caching sentiment labels for models and labels avoids repeated heavy computations — great performance optimization.
@lru_cache(maxsize=1)
def load_sentiment_labels():
    try:
        with open("sentiment_labels.json") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Sentiment labels configuration file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding sentiment labels configuration file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error loading sentiment labels: {str(e)}")


# Caching classifier pipeline for models and labels avoids repeated heavy computations — great performance optimization.
@lru_cache(maxsize=1)
def get_classifier():
    try:
        # classifier = pipeline("zero-shot-classification", model="bart-large-mnli") # Needs api key
        classifier = pipeline("zero-shot-classification")
        if not classifier:  # Extra safety check
            raise ValueError("Failed to initialize the classifier pipeline")
        return classifier
    except Exception as e:
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
                SentimentResult(label=label, score=round(score, 4))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SentimentResponse objects directly