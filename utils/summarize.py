# ./utils/summarize.py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import pipeline
from functools import lru_cache
from .logger import log_info, log_debug, log_error
import pandas as pd
import pprint as p
import numpy as np
import torch
import json

# Cache pipeline instance to avoid heavy object creation
@lru_cache(maxsize=1)
def get_summarize_pipeline():
    try:
        log_info(f"Initailizing summarization pipeline — {str(__file__)}")
        summarize_pipeline = pipeline(
            "summarization",
            model="google-t5/t5-base",
            tokenizer="google-t5/t5-base",
            framework="pt",
            clean_up_tokenization_spaces=True
        )
        if not summarize_pipeline:
            log_debug(f"Failed to load summarization pipeline — {str(__file__)}")
            raise ValueError("Failed to initialize the classifier pipeline")
        log_info("Summarization pipeline initialized successfully.")
        return summarize_pipeline
    except Exception as e:
        log_error(f"Unexpected error occured while initializing summarization pipeline — {str(__file__)} — {str(e)}")
        raise RuntimeError(f"Error initializing summarization pipeline — {str(e)}")
