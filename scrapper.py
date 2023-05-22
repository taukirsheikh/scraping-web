import requests
# url ="https://www.nepalnews.com/"
# r=requests.get(url)
# print(r.text) # gives the html or url content

def fetchAndSaveToFile(url, path):
    r=requests.get(url)
    with open(path,"w", encoding="utf-8") as scrapper:
        scrapper.write(r.text)
        print(r.json())
# url="https://www.nepalnews.com/"
url="https://merojob.com/"
fetchAndSaveToFile(url, "data/jobs.html")

