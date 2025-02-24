# ./models/sentiment.py

from functools import lru_cache
from transformers import pipeline
from fastapi import HTTPException
from .models import *
from typing import List
import sys

# classifier = pipeline("zero-shot-classification")

all_sentiment_labels = [
    "positive", "negative", "neutral", "politics", "education", "business",
    "technology", "sports", "joy", "anger", "sadness", "surprise", "fear",
    "question", "statement", "command",
]

# Break up sentiment types into groups for more comprehensive api usages

tone_sentiment_labels = [
    "positive", "negative", "neutral",
]

emotion_sentiment_labels = [
    "joy", "anger", "sadness", "surprise", "fear",
]

speech_sentiment_labels = [
    "question", "statement", "command",
]

profession_sentiment_labels = [
    "politics", "education", "business", "technology", "sports",
]


# Cache the classifier pipeline
@lru_cache(maxsize=1)
def get_classifier():
    try:
        classifier = pipeline("zero-shot-classification")
        if not classifier:  # Extra safety check
            raise ValueError("Failed to initialize the classifier pipeline")
        return classifier
    except Exception as e:
        raise RuntimeError(f"Error initializing classifier: {str(e)}")


# Function for retrieving sentiment analysis on data passed in
def get_sentiments(candidate_labels: List[str], prompts: List[str]) -> List[SentimentResponse]:
    classifier = get_classifier()  # cache the classifier object instance
    
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=candidate_labels)
            
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


# Function for retrieving sentiment analysis on data passed in
def get_all_sentiments(prompts: List[str]) -> List[SentimentResponse]:
    global all_sentiment_labels
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=all_sentiment_labels)
            
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


# Function for retrieving emotion sentiment analysis on data passed in
def get_emotion_sentiments(prompts: List[str]) -> List[SentimentResponse]:
    global emotion_sentiment_labels
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=emotion_sentiment_labels)
            
            # Create a list of SentimentResult objects
            sentiments = [
                SentimentResult(label=label, score=round(score, 4))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # # Print info about SentimentRequest (for testing)
            # sys.stdout(getattr(SentimentRequest, "__info__"))
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of EmotionSentimentResponse objects directly


# Function for retrieving tone sentiment analysis on data passed in
def get_tone_sentiments(prompts: List[str]) -> List[SentimentResponse]:
    global tone_sentiment_labels
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=tone_sentiment_labels)
            
            # Create a list of SentimentResult objects
            sentiments = [
                SentimentResult(label=label, score=round(score, 4))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # # Print info about SentimentRequest (for testing)
            # sys.stdout(getattr(SentimentRequest, "__info__"))
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SentimentResponse objects directly


# Function for retrieving speach sentiment analysis on data passed in
def get_speech_sentiments(prompts: List[str]) -> List[SentimentResponse]:
    global speech_sentiment_labels
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=speech_sentiment_labels)
            
            # Create a list of SentimentResult objects
            sentiments = [
                SentimentResult(label=label, score=round(score, 4))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # # Print info about SentimentRequest (for testing)
            # sys.stdout(getattr(SentimentRequest, "__info__"))
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SentimentResponse objects directly


# Function for retrieving profession sentiment analysis on data passed in
def get_profession_sentiments(prompts: List[str]) -> List[SentimentResponse]:
    global profession_sentiment_labels
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=profession_sentiment_labels)
            
            # Create a list of SentimentResult objects
            sentiments = [
                SentimentResult(label=label, score=round(score, 4))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # # Print info about SentimentRequest (for testing)
            # sys.stdout(getattr(SentimentRequest, "__info__"))
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SentimentResponse objects directly
