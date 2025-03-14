import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")


# Model Configuration
MODEL_NAME = "deepseek-chat"
MODEL_BASE_URL = "https://api.deepseek.com"

# Scoring Weights
SCORING_WEIGHTS = {
    "relevance": 0.3,
    "grammar": 0.2,
    "structure": 0.2,
    "depth": 0.3
}

# Minimum Scores for Progression
MIN_SCORES = {
    "relevance": 0.5,
    "grammar": 0.6,
    "structure": 0.7
} 