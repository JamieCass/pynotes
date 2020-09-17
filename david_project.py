import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

############### initial urls ###############

base_url = 'http://books.toscrape.com'
url = 'index.html'


res = requests.get(f'{base_url}/{url}')
soup = BeautifulSoup(res.text, 'html.parser')
############### list of the book pages ###############

books = soup.find_all('article')

all_books = []
for book in books:
    book_link = book.find('a')['href']
    all_books.append(book_link)
all_books

############### go to the next page ###############
next_btn = soup.find(class_='next')
url = next_btn.find('a')['href'] if next_btn else None
url
