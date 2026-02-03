import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set")

genai.configure(api_key=API_KEY)

def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.3,
    )
