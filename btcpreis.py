import requests
from bs4 import BeautifulSoup

response = requests.get("https://bitcoin.de")
soup = BeautifulSoup(response.content, "html.parser")

btc_price = soup.find(id="ticker_price")
print(btc_price)