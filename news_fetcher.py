import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=20&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    headlines = []

    if "articles" in data:

        for article in data["articles"]:

            title = article.get("title")

            if title:
                headlines.append(title)

    return headlines