import requests
from bs4 import BeautifulSoup
with open("data/jobs.html", "r", encoding='utf-8') as f: # r is read mode
    html_doc=f.read()
#the soup object passes the html doc and the parser string
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title) #gives element
# print(soup.title.name) #gives the tag name
# print(soup.title.string) #gives the text in the element 
# print(soup.div) # gives the first div
# print(soup.find_all('div') [2])
# to get all text
# print(soup.get_text()) 
for link in soup.find_all("a"):
    # print(link.get("href"))
    # print(link.get("href").getText())
    # print(link.text)
    print(link.get_text())