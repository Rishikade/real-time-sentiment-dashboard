from news_fetcher import get_news

news = get_news("Tesla")

for item in news:
    print(item)