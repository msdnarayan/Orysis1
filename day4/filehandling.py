from bs4 import BeautifulSoup
import requests

# response=requests.get("https://www.ycombinator.com/")
# print(response)


file=open("index.html")
contents=file.read()#print(contents)
file.close()

soup=BeautifulSoup(contents,"html.parser")
all_links=soup.find_all(name="a")
for link in all_links:
    print(link.getText())
# first_heading=soup.find_all(class_="headings")
# print(first_heading)