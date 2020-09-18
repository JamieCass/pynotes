import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

############### initial urls ###############

base_url = 'http://books.toscrape.com'
url = 'page-1.html'
all_books = []

while url:
    res = requests.get(f'{base_url}/catalogue/{url}')
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
