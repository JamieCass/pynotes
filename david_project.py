import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3
import time
import urllib
from urllib.parse import urljoin
from csv import writer
from csv import reader

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
b_title = []
b_price = []
b_rating = []
b_upc = []
b_stock = []
b_description = []

def book_page_open(site):
    '''
    request the site
    parse into bs
    find title, price, rating, upc, stock and desription
    '''
    b_page = requests.get(site)
    bsoup = BeautifulSoup(b_page.text, 'html.parser')
    prod_title = soup1.find('h1').text
    b_title.append(prod_title)

    prod_price = bsoup.find(class_='price_color').text
    new_price = float(prod_price.replace('£','').replace('Â',''))
    b_price.append(new_price)

    ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    rate = bsoup.select('.star-rating')[0]
    rating_word = rate.get_attribute_list('class')[-1]
    prod_rating = ratings[rating_word]
    b_rating.append(prod_rating)

    table = bsoup.find(class_= 'table table-striped')
    prod_upc = table.find('td').get_text()
    b_upc.append(prod_upc)

    prod_stock = bsoup.find(class_='instock availability').text
    prod_stock = prod_stock.replace('\n', '').replace('  ','').replace('(','').replace(')','').split()
    stock_num = prod_stock[-2]
    b_stock.append(stock_num)

    desc = bsoup.find(class_='product_page').find_all('p')
    prod_desc = desc[-1].text
    b_description.append(prod_desc)



book_page = base_url
book_page
next_b_page = urljoin(book_page,all_books[0])
next_b_page
title = []
price = []
rating = []
upc = []
stock = []
description = []


for i in all_books[1:4]:
    print('current_page:', next_b_page)
    book_page_open(next_b_page)
    title.append(b_title)
    price.append(b_price)
    rating.append(b_rating)
    upc.append(b_upc)
    stock.append(b_stock)
    description.append(b_description)
    next_b_page = urljoin(book_page, i)

title

############################## save all info into a csv file ##############################
def write_book(books):
    '''
    save all book info to either dict or normal csv file
    '''

######################################################## TEST ########################################################
test = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

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
stock = stock.replace('\n', '').replace('  ','').replace('(','').replace(')','').split()
stock
stock_num = stock[-2]
stock_num

################# DESCRIPTION #################
desc = soup1.find(class_='product_page').find_all('p')
description = desc[-1].text
