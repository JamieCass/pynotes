from bs4 import BeautifulSoup
import requests
from csv import reader
from csv import writer
import urllib
from urllib.parse import urljoin


site = 'http://quotes.toscrape.com'
r = requests.get(site)
soup = BeautifulSoup(r.text, 'html.parser')
#
# print(r.text)

# for i in range(1,11):      # Number of pages plus one
#     url = "http://quotes.toscrape.com/page/{}".format(i)
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')

print(r.text)
# --------- testing some stuff out ---------


trial = soup.find_all(class_ = 'quote')

for x in trial:
    text2 = soup.find_all(class_ = 'text')
new = [x.text for x in text2]
new

davids = [x.find('a') for x in trial]
davids

def webIterate():
    count = 1
    base_link = "http://quotes.toscrape.com/"
    while count <= 11:
        yield count
        count +=1
    return f'http://quotes.toscrape.com/page/{count}'

next_page = soup.find_all(class_ = 'next')
next_page
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
project_href = [i['href'] for i in soup.find_all('a', href=True)]
project_href

keywords = ['author']
author_links = [link for link in project_href if all(keyword in link for keyword in keywords)]
author_links


albert = site + author_links[0]
albert
alb_bio = requests.get(albert)
print(alb_bio.text)

al_soup = BeautifulSoup(alb_bio.text, 'html.parser')
alb_info = []
alb_dob = al_soup.find(class_ = 'author-born-date')
alb_info.append(alb_dob.text)
alb_loc = al_soup.find(class_ = 'author-born-location')
alb_info.append(alb_loc.text)
alb_desc = al_soup.find(class_ = 'author-description')
alb_info.append(alb_desc.text.replace('\n', ''))

alb_info
