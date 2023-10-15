from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
#print(response)

soup=BeautifulSoup(response.text,"lxml")

first_heading=soup.find_all(class_="athing")
#print(first_heading)

for txt in first_heading:
    print(txt.getText())