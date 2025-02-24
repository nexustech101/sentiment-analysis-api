# ./models/sentiment.py

from transformers import pipeline
from fastapi import HTTPException
from .models import *
from typing import List

classifier = pipeline("zero-shot-classification")

candidate_labels = [
    "positive", "negative", "neutral", "politics", "education", "business",
    "technology", "sports", "joy", "anger", "sadness", "surprise", "fear",
    "question", "statement", "command"
]

def get_sentiment_analysis(prompts: List[str]) -> List[SentimentResponse]:
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
                SentimentResult(label=label, score=round(score, 3))
                for label, score in zip(res['labels'], res['scores'])
            ]
            
            # Create a SentimentResponse object
            sentiment_response = SentimentResponse(sequence=prompt, sentiments=sentiments)
            
            results.append(sentiment_response)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing prompt: {str(e)}")
    
    return results  # Return list of SentimentResponse objects directly


# if __name__ == "__main__":
#     prompts = [
#         "The new AI model has been making waves in the tech industry.",
#         "I’m so excited to start this new adventure!",
#         "Why is the sky blue?",
#         "The economy is showing signs of improvement.",
#         "Let’s schedule a meeting for next week.",
#         "The football team won the championship last night.",
#         "I’m feeling a bit under the weather today.",
#         "This new smartphone has incredible features.",
#         "We should focus on renewable energy sources.",
#         "Can you help me with this math problem?",
#         "The concert was absolutely amazing!",
#         "Political debates often get heated.",
#         "Our science class is learning about photosynthesis.",
#         "The stock market took a sharp downturn yesterday.",
#         "I think we need a different approach to this project.",
#         "Why do cats purr?",
#         "The teacher explained the concept very clearly.",
#         "There’s been a lot of buzz around electric vehicles.",
#         "I’m really scared of public speaking.",
#         "The weather forecast predicts heavy rain tomorrow.",
#         "We need to discuss our business strategy moving forward.",
#         "Artificial intelligence is transforming the job market.",
#         "I’m so happy with the results of my exam!",
#         "Could you please clarify your statement?",
#         "The movie’s plot twist was completely unexpected."
#     ]
#     get_sentiment_analysis(prompts=prompts)
