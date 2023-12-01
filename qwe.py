import requests
from bs4 import BeautifulSoup
from time import sleep

for count in range(1, 7): # Добавили еще один цикл

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}" # f-строка и count

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data:
        name = i.find("h4").text
        price = i.find("h5").text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

        print(name + '\n' + price + '\n' + url_img + '\n\n')