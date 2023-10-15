from bs4 import BeautifulSoup
import requests

res=requests.get("https://amzn.eu/d/8wID6vw")

soup=BeautifulSoup(res.text,"lxml")

price=soup.find_all('span',class_="a-price-whole")

for txt in price:
#     print(price.select('.a-price-whole'))
    print("The Price of"txt.getText())
#     product_price = price.get_text(strip=True)
#     print(product_price)
#     txt.append(str(price.text).strip())
#     print(price)
#print(price)
