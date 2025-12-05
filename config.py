import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------
# AI Keys
# ---------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ---------------------------
# Deployment Tokens
# ---------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
VERCEL_TOKEN = os.getenv("VERCEL_TOKEN")
RENDER_TOKEN = os.getenv("RENDER_TOKEN")
RAILWAY_TOKEN = os.getenv("RAILWAY_TOKEN")