from fetch_news import fetch_news
from fetch_tweets import fetch_tweets
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_text(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text

texts = fetch_tweets("earthquake") + fetch_news()
summaries = [analyze_text(text) for text in texts]
print(summaries)