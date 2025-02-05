import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = [h.text for h in soup.find_all("h3")]
    return headlines