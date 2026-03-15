import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.craigslist.org"

def fetch_craigslist(city="yourcity"):
    url = f"https://{city}.craigslist.org/search/rea"
    res = requests.get(url, timeout=10)

    soup = BeautifulSoup(res.text, "html.parser")
    listings = []

    for row in soup.select(".result-row"):
        title = row.select_one(".result-title").text
        price = row.select_one(".result-price")
        price = int(price.text.replace("$", "")) if price else None
        link = row.select_one(".result-title")["href"]

        listings.append({
            "title": title,
            "price": price,
            "url": link,
            "source": "craigslist"
        })

    return listings
