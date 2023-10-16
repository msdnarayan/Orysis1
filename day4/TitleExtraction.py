from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
#print(response)

soup=BeautifulSoup(response.text,"lxml")

heading=soup.find_all("span",class_="titleline")
score=soup.find_all("span",class_="score")
#print(first_heading)

headings=[]
links=[]
scores=[]
for txt in heading:
    link = txt.find("a")
    headings.append(link.getText())
    links.append(link.get("href"))

for scoress in score:
    scores.append(scoress.getText())
    

print(headings)
print(links)
print(scores)