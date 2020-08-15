from bs4 import BeautifulSoup
import requests
from csv import reader
from csv import writer
import urllib
from urllib.parse import urljoin


site = 'http://quotes.toscrape.com'
r = requests.get(site)
soup = BeautifulSoup(r.text, 'html.parser')

print(r.text)

quotes = soup.find_all('div', class_ = 'quote')
quotes

quotes[0].find('span', class_ = 'text').text

quotes[0].find('small', class_ = 'author').text

quote_list = []
author_list = []
for quote in quotes:
    text = quote.find('span', class_ = 'text').text
    quote_list.append(text)
    author = quote.find('small', class_ = 'author').text
    author_list.append(author)

next_page = soup.find(class_ = 'next')
next_page_url = next_page.find('a')['href']
next_page_url

def page_open(site):
    '''
    request the site
    parse into bs
    find quotes and authors
    find next page
    '''

    r = requests.get(site)
    soup = BeautifulSoup(r.text, 'html.parser')

    quotes = soup.find_all('div', class_ = 'quote')

    quote_list = []
    author_list = []
    for quote in quotes:
        text = quote.find('span', class_ = 'text').text
        quote_list.append(text)
        author = quote.find('small', class_ = 'author').text
        author_list.append(author)

    next_page = soup.find(class_ = 'next')
    next_page_url = next_page.find('a')['href']
    next_page_url

    return quote_list, author_list, next_page_url

quotes_all = []
authors_all = []
site = 'http://quotes.toscrape.com'
next_page = site
for i in range(10):
    quote_text, author_names, next_page_url = page_open(next_page)

    quotes_all = quotes_all + quote_text

    authors_all = authors_all + author_names

    next_page = urljoin(site, next_page_url)
