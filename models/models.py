# ./models/models.py

from pydantic import BaseModel
from typing import List, Dict

# Full sentiment analysis models (abstracts away models for comprehensive documentation and api usage)
class FullSentimentRequest(BaseModel):
    prompts: List[str]
    __info__: str = None


class FullSentimentResult(BaseModel):
    label: str
    score: float
    __info__: str = None


class FullSentimentResponse(BaseModel):
    sequence: str
    sentiments: List[SentimentResult]
    __info__: str = None


# Emotion sentiment models (abstracts away models for comprehensive documentation and api usage)
class EmotionSentimentRequest(SentimentRequest):
    __info__: str = "Inherits from SentimentRequest parent model"


class EmotionSentimentResult(SentimentResult):
    __info__: str = "Inherits from SentimentResult parent model"


class EmotionSentimentResponse(SentimentResponse):
    __info__: str = "Inherits from SentimentResponse parent model"


# Tonality sentiment models (abstracts away models for comprehensive documentation and api usage)
class ToneSentimentRequest(SentimentRequest):
    __info__: str = "Inherits from SentimentRequest parent model"


class ToneSentimentResult(SentimentResult):
    __info__: str = "Inherits from SentimentResult parent model"


class ToneSentimentResponse(SentimentResponse):
    __info__: str = "Inherits from SentimentResponse parent model"


# Speach sentiment models (abstracts away models for comprehensive documentation and api usage)
class SpeachSentimentRequest(SentimentRequest):
    __info__: str = "Inherits from SentimentRequest parent model"


class SpeachSentimentResult(SentimentResult):
    __info__: str = "Inherits from SentimentResult parent model"


class SpeachSentimentResponse(SentimentResponse):
    __info__: str = "Inherits from SentimentResponse parent model"


# Speach sentiment models (abstracts away models for comprehensive documentation and api usage)
class SpeachSentimentRequest(SentimentRequest):
    __info__: str = "Inherits from SentimentRequest parent model"


class SpeachSentimentResult(SentimentResult):
    __info__: str = "Inherits from SentimentResult parent model"


class SpeachSentimentResponse(SentimentResponse):
    __info__: str = "Inherits from SentimentResponse parent model"