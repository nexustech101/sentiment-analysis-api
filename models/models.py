# ./models/models.py

from pydantic import BaseModel
from typing import List, Dict

# Base model to be inherited by al other sentiment models
class Base(BaseModel):
    __info__: str = "Inherits from SentimentRequest parent (Base) model"


# Full sentiment analysis models (abstracts away models for comprehensive documentation and api usage)
class FullSentimentRequest(Base):
    prompts: List[str]


class FullSentimentResult(Base):
    label: str
    score: float


class FullSentimentResponse(Base):
    sequence: str
    sentiments: List[FullSentimentResult]


# Emotion sentiment models (abstracts away models for comprehensive documentation and api usage)
class EmotionSentimentRequest(FullSentimentRequest):
    pass


class EmotionSentimentResult(FullSentimentResult):
    pass


class EmotionSentimentResponse(FullSentimentResponse):
    pass


# Tonality sentiment models (abstracts away models for comprehensive documentation and api usage)
class ToneSentimentRequest(FullSentimentRequest):
    pass


class ToneSentimentResult(FullSentimentResult):
    pass


class ToneSentimentResponse(FullSentimentResponse):
    pass


# Speach sentiment models (abstracts away models for comprehensive documentation and api usage)
class SpeachSentimentRequest(FullSentimentRequest):
    pass


class SpeachSentimentResult(FullSentimentResult):
    pass


class SpeachSentimentResponse(FullSentimentResponse):
    pass


# Profession sentiment models (abstracts away models for comprehensive documentation and api usage)
class ProfessionSentimentRequest(FullSentimentRequest):
    pass


class ProfessionSentimentResult(FullSentimentResult):
    pass


class ProfessionSentimentResponse(FullSentimentResponse):
    pass