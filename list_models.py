import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads GOOGLE_API_KEY from .env file

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in .env file")

genai.configure(api_key=api_key)

print("\n=== AVAILABLE GEMINI MODELS ===\n")

models = genai.list_models()

for m in models:
    name = m.name
    methods = getattr(m, "supported_generation_methods", None)
    print(f"{name}  |  supported: {methods}")

print("\n================================\n")
