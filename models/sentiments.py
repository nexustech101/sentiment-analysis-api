# ./models/sentiment.py

from transformers import pipeline
from fastapi import HTTPException
from .models import *
from typing import List
import sys

classifier = pipeline("zero-shot-classification")

all_sentiment_labels = [
    "positive", "negative", "neutral", "politics", "education", "business",
    "technology", "sports", "joy", "anger", "sadness", "surprise", "fear",
    "question", "statement", "command"
]

# Break up sentiment types into groups for more comprehensive api usages

tone_sentiment_labels = [
    "positive", "negative", "neutral",
]

emotion_sentiment_labels = [
    "joy", "anger", "sadness", "surprise", "fear",
]

speach_sentiment_labels = [
    "question", "statement", "command",
]

profession_sentiment_labels = [
    "politics", "education", "business", "technology", "sports",
]

# Function for retrieving full sentiment analysis on data passed in
def get_all_sentiments(prompts: List[str]) -> List[FullSentimentResponse]:
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=all_sentiment_labels)
            
            # Create a list of FullSentimentResult objects
            sentiments = [
                FullSentimentResult(label=label, score=round(score, 3))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Create a FullSentimentResponse object
            sentiment_response = FullSentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of FullSentimentResponse objects directly


# Function for retrieving emotion sentiment analysis on data passed in
def get_emotion_sentiments(prompts: List[str]) -> List[EmotionSentimentResponse]:
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=emotion_sentiment_labels)
            
            # Create a list of EmotionSentimentResult objects
            sentiments = [
                EmotionSentimentRequest(label=label, score=round(score, 3))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Print info about EmotionSentimentRequest
            sys.stdout(getattr(EmotionSentimentRequest, "__info__"))
            
            # Create a EmotionSentimentResponse object
            sentiment_response = EmotionSentimentRequest(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of EmotionSentimentResponse objects directly


# Function for retrieving tone sentiment analysis on data passed in
def get_tone_sentiments(prompts: List[str]) -> List[ToneSentimentResponse]:
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=tone_sentiment_labels)
            
            # Create a list of ToneSentimentResult objects
            sentiments = [
                ToneSentimentRequest(label=label, score=round(score, 3))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Print info about ToneSentimentRequest
            sys.stdout(getattr(ToneSentimentRequest, "__info__"))
            
            # Create a ToneSentimentResponse object
            sentiment_response = ToneSentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of ToneSentimentResponse objects directly


# Function for retrieving speach sentiment analysis on data passed in
def get_speach_sentiments(prompts: List[str]) -> List[SpeachSentimentResponse]:
    if not prompts:
        raise ValueError("Prompts list cannot be empty")
    
    results = []
    
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip():
            continue
        try:
            res = classifier(prompt, candidate_labels=speach_sentiment_labels)
            
            # Create a list of SpeachSentimentResult objects
            sentiments = [
                SpeachSentimentRequest(label=label, score=round(score, 3))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Print info about SpeachSentimentRequest
            sys.stdout(getattr(SpeachSentimentRequest, "__info__"))
            
            # Create a SentimentResponse object
            sentiment_response = SpeachSentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SpeachSentimentResponse objects directly
