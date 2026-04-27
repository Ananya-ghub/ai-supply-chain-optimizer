from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
import json
import logging

# ------------------ LOGGING ------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ------------------ ENV ------------------
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    logger.warning("API_KEY is not set in environment variables. Make sure to add it to your .env file.")

# ------------------ APP ------------------
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Smart Supply Chain Optimization API",
    description="AI-powered system to analyze shipment data and predict delay risks.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ MODEL ------------------
class ShipmentData(BaseModel):
    source: str
    destination: str
    delay: str
    weather: str
    traffic: str

# ------------------ PROMPT ------------------
def build_prompt(data: ShipmentData) -> str:
    return f"""
You are a logistics optimization AI.

Analyze this shipment:

Source: {data.source}
Destination: {data.destination}
Delay: {data.delay}
Weather: {data.weather}
Traffic: {data.traffic}

Return ONLY valid JSON:

{{
  "risk": number (0-100),
  "reason": "string",
  "suggestion": "string"
}}
"""

# ------------------ GEMINI CALL ------------------
def call_gemini(prompt: str) -> dict:
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key is missing on the server.")

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code != 200:
            print("FULL ERROR:", response.text)
            raise HTTPException(status_code=502, detail=response.text)

        return response.json()

    except Exception as e:
        print("EXCEPTION:", str(e))
        raise HTTPException(status_code=502, detail=str(e))
# ------------------ PARSE RESPONSE ------------------
def extract_json(gemini_response: dict) -> dict:
    try:
        text = gemini_response["candidates"][0]["content"]["parts"][0]["text"].strip()

        # Clean markdown if exists
        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        data = json.loads(text)

        return {
            "risk": float(data.get("risk", 0)),
            "reason": data.get("reason", ""),
            "suggestion": data.get("suggestion", "")
        }

    except Exception as e:
        logger.error(f"Parsing error: {e}")
        raise HTTPException(status_code=500, detail="Invalid AI response format.")

# ------------------ ROUTES ------------------
@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/analyze")
def analyze(data: ShipmentData):
    prompt = build_prompt(data)
    ai_response = call_gemini(prompt)
    result = extract_json(ai_response)
    return result