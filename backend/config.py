import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Explicitly configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.3,
    )