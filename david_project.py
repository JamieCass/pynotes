import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3
import time
import urllib
from urllib.parse import urljoin
from csv import writer
from csv import reader
import pandas as pd

############################## all book urls ##############################

base_url = 'http://books.toscrape.com/catalogue/'
url = 'page-1.html'
all_books = []

while url:
    res = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(res.text, 'html.parser')

    ############### list of the book pages ###############

    books = soup.find_all('article')

    for book in books:
        all_books.append(book_link)
        book_link = book.find('a')['href']

    ############### go to the next page ###############
    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None

all_books
all_books[0]

############################## loop all book urls ##############################


def book_page_open(site):
    '''
    request the site
    parse into bs
    find title, price, rating, upc, stock and desription
    '''


    b_page = requests.get(site)
    bsoup = BeautifulSoup(b_page.text, 'html.parser')
    title = bsoup.find('h1').text


    prod_price = bsoup.find(class_='price_color').text
    price = float(prod_price.replace('£','').replace('Â',''))


    ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    rate = bsoup.select('.star-rating')[0]
    rating_word = rate.get_attribute_list('class')[-1]
    rating = ratings[rating_word]


    table = bsoup.find(class_= 'table table-striped')
    upc = table.find('td').get_text()

    prod_stock = bsoup.find(class_='instock availability').text
    # prod_stock = prod_stock.replace('\n', '').replace('  ','').replace('(','').replace(')','').split('\n')
    stock = prod_stock[prod_stock.find('(')+1:prod_stock.find('available')-1]

    desc = bsoup.find(class_='product_page').find_all('p')
    desc = [x for x in desc if x.attrs=={}]
    desc = desc[0].text

    src = bsoup.find('img')
    img_src = next(iter(src.attrs.values())).replace('../..','')

    sleep(0.5)

    return title, price, rating, upc, stock, desc, img_src


all_book_info = []

for i in all_books:
    print('current_page:', base_url,i)
    title, price, rating, upc, stock, desc, img_src  = book_page_open(urljoin(base_url, i))
    all_book_info.append([upc, title, price, rating, stock, img_src, desc])
    # next_b_page = urljoin(book_page, i

all_book_info
df = pd.DataFrame(all_book_info, columns=['UPC', 'Title', 'Price', 'Rating', 'Stock', "Img_src", 'Description'])
df

######################################################## TEST ########################################################
test = 'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'

res1 = requests.get(test)
soup1 = BeautifulSoup(res1.text, 'html.parser')

################# TITLE #################
title = soup1.find('h1').text
title

################# PRICE #################
price = soup1.find(class_='price_color').text
new_price = float(price.replace('£','').replace('Â',''))
new_price

################# RATING #################
ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
rate = soup1.select('.star-rating')[0]
rating_word = rate.get_attribute_list('class')[-1]
rating = ratings[rating_word]
rating

################# UPC #################
table = soup1.find(class_= 'table table-striped')
upc = table.find('td').get_text()
upc

################# STOCK #################
stock = soup1.find(class_='instock availability').text
stock
stock
stock[stock.find('(')+1:stock.find('available')-1]

################# DESCRIPTION #################
desc = soup1.find(class_='product_page').find_all('p')

desc = soup1.find(class_='product_page').find_all('p')
desc = [x for x in desc if x.attrs=={}]
desc = desc[0].text
desc

desc = [x for x in desc if x.attrs=={}]
desc = desc[0].text
for x in desc:
    if x.attrs=={}:

        print(x.attrs, ' '.join(x.text.split()))
        print('-'*40)
dir(desc[0])

type(desc)
len(desc)
description = desc.text
desc

################# IMAGE SRC #################
src = soup1.find('img')
img_src = next(iter(src.attrs.values())).replace('../..','')
img_src
dir(src)
