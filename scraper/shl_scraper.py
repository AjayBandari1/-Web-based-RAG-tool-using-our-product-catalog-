
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shl_catalog(base_url):
    results = []
    session = requests.Session()

    for page in range(1, 3):
        response = session.get(f"{base_url}?page={page}")
        soup = BeautifulSoup(response.text, "html.parser")

        for card in soup.select("a"):
            title = card.text.strip()
            link = card.get("href")
            if title and link:
                results.append({"title": title, "url": link})

    df = pd.DataFrame(results)
    df.to_csv("data/shl_catalog_scraped.csv", index=False)
    return df
