# Sentiment Analysis API

## Project Overview
This project is a FastAPI-based sentiment analysis API. It provides endpoints for analyzing the sentiment of text inputs and is structured for scalability, modularity, and performance. The API leverages pre-labeled sentiment data and includes efficient caching, error logging, and a well-organized directory structure.

## Features
- FastAPI framework for high-performance API development
- Modular architecture for models, routes, and utilities
- Sentiment analysis using pre-labeled data
- Efficient caching with `@lru_cache`
- Structured error handling and logging
- Pydantic models for request validation and response consistency

## Project Structure
```
C:.
│   .gitignore
│   error.log                   # Error logging file
│   main.py                     # Entry point for the FastAPI application
│   README.md                   # Project documentation
│   requirements.txt            # Python dependencies
│   run.sh                      # Shell script to run the API
│   sentiment_labels.json       # Sentiment data
│
├───docs
│       docs.md                 # Additional project documentation
│
├───models
│       models.py               # Pydantic models for API data validation
│       __init__.py             # Package initializer
│
├───routers
│       sentiment_route.py      # API route for sentiment analysis
│       __init__.py             # Package initializer
│
├───test
│       output.json             # Sample test output
│       sentiment.test.py       # Test cases for sentiment analysis
│
└───utils
        sentiment_utils.py      # Utility functions for sentiment analysis
        __init__.py             # Package initializer
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-repo/sentiment-analysis-api.git
```

2. Navigate to the project directory:
```bash
cd sentiment-analysis
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API
For Windows:
```bash
run.cmd
```

For Linux/Mac:
```bash
bash run.sh
```

Or run directly with Python:
```bash
uvicorn main:app --reload
```

API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints
### `POST /sentiment`
Analyzes the sentiment of the provided text.

**Request:**

```json
{
  "prompts": [
    "I'm going to teach a lesson on python best practices."
  ]
}
```

**Response example:**

```json
{
  "sentiment": "positive",
  "confidence": 0.98
}
```
##### or

```json
[
  {
    "sequence": "The new AI model has been making waves in the tech industry.",
    "sentiments": [
      { "label": "technology", "confidence": 0.831 },
      { "label": "surprise", "confidence": 0.048 },
      { "label": "statement", "confidence": 0.034 },
      { "label": "question", "confidence": 0.029 },
      { "label": "positive", "confidence": 0.014 },
      { "label": "command", "confidence": 0.011 },
      { "label": "business", "confidence": 0.009 },
      { "label": "joy", "confidence": 0.007 },
      { "label": "neutral", "confidence": 0.004 },
      { "label": "negative", "confidence": 0.003 },
      { "label": "fear", "confidence": 0.002 },
      { "label": "sports", "confidence": 0.002 },
      { "label": "anger", "confidence": 0.002 },
      { "label": "education", "confidence": 0.002 },
      { "label": "politics", "confidence": 0.001 },
      { "label": "sadness", "confidence": 0.001 }
    ]
  },
]
```

## Testing
Run tests with:
```bash
pytest test/sentiment.test.py
```

## Logging
Errors are logged to `error.log`.

## Contributing
1. Fork the repo.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

