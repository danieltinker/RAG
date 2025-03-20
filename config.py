# config.py

import os
import logging
import sys
from dotenv import load_dotenv

# =============================================================================
# Configuration & Logging Setup
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# Load variables from .env into the environment
load_dotenv()

# Access the secret from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# API & Model Configuration
EMBEDDING_MODEL = 'text-embedding-3-small'
