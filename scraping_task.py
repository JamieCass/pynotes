from bs4 import BeautifulSoup
import requests
from csv import reader
from csv import writer



for i in range(11):      # Number of pages plus one
    site = 'http://quotes.toscrape.com/'.format(i)
    r = requests.get(site)
    soup = BeautifulSoup(r.text, 'html.parser')




# --------- testing some stuff out ---------

trial = soup.find_all(class_ = 'quote')

for x in trial:
    text2 = soup.find_all(class_ = 'text')
new = [x.text for x in text2]
new

davids = [x.find('a') for x in trial]
davids

def webIterate():
    base_link = "http://quotes.toscrape.com/"
    for i in range(11):
        return f'http://quotes.toscrape.com/page/{i}'
webIterate()

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
