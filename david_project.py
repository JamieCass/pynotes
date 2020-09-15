import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

base_url = 'http://books.toscrape.com'
url = '/index.html'

res = requests.get(f'{base_url}{url}')
soup = BeautifulSoup(res.text, 'html.parser')

############### go to the next page ###############
next_btn = soup.find(class_='next')
url = next_btn.find('a')['href'] if next_btn else None
