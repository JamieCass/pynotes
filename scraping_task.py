from bs4 import BeautifulSoup
import requests
from csv import reader
from csv import writer

site = 'http://quotes.toscrape.com/'
response = requests.get(site)

print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')


# --------- testing some stuff out ---------

trial = soup.find_all(class_ = 'quote')

for x in trial:
    text2 = soup.find_all(class_ = 'text')
new = [x.text for x in trial]
new

# ------------------------------------------


# TEXT OF QUOTES
text = soup.select('.text')
quotes = [x.text for x in text]
quotes


# NAME OF PERSON
author = soup.select('.author')
authors = [x.text for x in author]
authors


# HREF OF LINK
links = soup.find_all('span')
type(links)
dir(links)
links
for link in links:
    url = link.find('a')
print(url[0])
project_href = [i['href'] for i in soup.find_all('a', href=True)]
project_href

keywords = ['author']

for link in project_href:
    if all(keyword in link for keyword in keywords):
        print(link)
author_links = [link for link in project_href if all(keyword in link for keyword in keywords)]
author_links
