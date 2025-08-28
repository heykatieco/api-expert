# Use resource library to import and display article
import json
import os
import requests
from dotenv import load_dotenv

from article import Article

load_dotenv()

api_key = os.getenv('API_KEY')


url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-08-15&'
       'sortBy=popularity&'
       f'apiKey={api_key}'
       )


try:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        articles = response.json()['articles']
        article_objects = []
        for article in articles:
            article = Article(article)
            article_objects.append(article)

        if article_objects:
            print(f"First article: {article_objects[0].title}")
            print(f"Articles length: {len(article_objects)}")

except requests.exceptions.HTTPError as err:
    print(err)



