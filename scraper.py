from bs4 import BeautifulSoup
import requests
import pandas as pd
from pymongo import MongoClient
url = "https://www.ft.com/"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")
articles = soup.find_all("article")
blockchain_articles = []
for article in articles:
    if "blockchain" in article.text.lower():
        title = article.find("h3").text.strip()
        link = article.find("a")["href"]
        blockchain_articles.append({"title": title, "link": link})
client = MongoClient("mongodb://localhost:27017/")
db = client["blockchain_articles"]
collection = db["articles"]
collection.insert_many(blockchain_articles)
