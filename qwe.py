import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml') # html.parser - аналог lxml

data = soup.find_all("div", class_="w-full rounded border")

for i in data:
    name = i.find("h4").text
    price = i.find("h5").text
    url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

    print(name + '\n' + price + '\n' + url_img + '\n\n')


'''name = data.find("h4")

name = data.find("h4").text

price = data.find("h5").text

url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")'''


fl = open('proba.txt','w', encoding = 'utf-8')
print(data, file = fl)
fl.close()
