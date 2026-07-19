# Central configuration file for FinTwin AI.

from pathlib import Path
from dotenv import load_dotenv
import os

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
KNOWLEDGE_BASE_DIR = DATA_DIR / "knowledge_base"
MODEL_DIR = BASE_DIR / "models"

# Load environmental variables
load_dotenv(BASE_DIR / ".env")

# Application
APP_NAME = "FinTwin AI"
APP_TAGLINE = "Your Financial Digital Twin for Smarter Financial Decisions."

# PostgreSQL configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "fintwin_ai")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Groq configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Recommended default model
GROQ_MODEL = "llama-3.3-70b-versatile"

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ChromaDB
CHROMA_DB_PATH = str(BASE_DIR / "vector_store")

# Session
SESSION_TIMEOUT_MINUTES = 60

# Supported uploads
SUPPORTED_DOCUMENTS = [
    ".pdf"
]

# Financial health score
MAX_FINANCIAL_SCORE = 100

# Create required directories automatically
REQUIRED_DIRECTORIES = [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    KNOWLEDGE_BASE_DIR,
    MODEL_DIR,
    Path(CHROMA_DB_PATH)
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

