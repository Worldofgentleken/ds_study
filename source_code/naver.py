import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://finance.naver.com/marketindex/'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")
# print(soup.prettify)

exchangeList = soup.select("#exchangeList > li")


exchange_datas = []
baseUrl = "http://finance.naver.com"

for item in exchangeList:
    data = {
        "title" : item.select_one(".h_lst").text,
        "exchange" : item.select_one(".value").text,
        "change" : item.select_one(".change").text,
        "updown" : item.select_one("div.head_info.point_up > .blind").text,
        "link" : baseUrl + item.select_one("a").get("href")
    }
    exchange_datas.append(data)
df = pd.DataFrame(exchange_datas)
df.to_excel("./naverfinance.xlsx")