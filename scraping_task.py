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
new = [x.text for x in text2]
new

davids = [x.find('a') for x in trial]
davids

page_list = [c['href'] for c in soup.find_all('a')]
page_list
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


albert = site + author_links[0]
albert
alb_bio = requests.get(albert)
print(alb_bio.text)

al_soup = BeautifulSoup(alb_bio.text, 'html.parser')
alb_info = []
alb_dob = al_soup.find(class_ = 'author-born-date')
print(alb_description)
alb_info.append(alb_dob.text)
alb_info
alb_loc = al_soup.find(class_ = 'author-born-location')
alb_info.append(alb_loc.text)
alb_desc = al_soup.find(class_ = 'author-description')
alb_info.append(alb_desc.text)
