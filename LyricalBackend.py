from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Replace this with your Gemini API key
os.environ["API_KEY"] = os.getenv('API_KEY') 
genai.configure(api_key=os.environ["API_KEY"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify domains like ["https://your-frontend-url.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Base model for the input
class LyricsRequest(BaseModel):
    description: str

@app.post("/generate_lyrics")
def generate_lyrics(request: LyricsRequest):
    description = request.description
    # Send request to Gemini API
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(description)  # Hypothetical field for lyrics
        return {"lyrics": response.text}
    except requests.exceptions.HTTPError as err:
        raise HTTPException(status_code=response.status_code, detail=str(err))


# Start the app using this command:
# uvicorn app:app --reload
