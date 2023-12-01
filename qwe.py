import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml') # html.parser - аналог lxml

data = soup.find("div", class_="w-full rounded border")

name = data.find("h4")

name = data.find("h4").text

price = data.find("h5").text

url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")


fl = open('proba.txt','w', encoding = 'utf-8')
print(url_img, file = fl)
fl.close()
