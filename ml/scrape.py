from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("https://" +url)

data = r.text

soup = BeautifulSoup(data)

letters = soup.find_all("div", class_ = "grid")

dict = {'link': 'ha', 'src': 'ha', 'title':'ha', 'des': 'ha' }

f = open("news.txt","w")
mat = []
count = 0
for elements in letters:
    dict['link'] = letters[count].a["href"]
    dict['src'] = letters[count].a["title"]
    dict['title'] = letters[count].img["src"]
    text = letters[count].find_all("div", class_="visual_desc")
    dict['des'] = text[0].find_all("p")
    f.write(dict['link'])
    f.write("\n")
    f.write(dict['src'].encode('ascii','ignore'))
    f.write("\n")
    f.write(dict['title'])
    f.write("\n")
    f.write(str(dict['des']))
    f.write("\n")
    f.write("\n")
    count  += 1

f.close()