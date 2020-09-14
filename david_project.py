import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

base_url = 'https://www.kingsoopers.com'
dairy = '/pl/dairy-eggs/18007'

res = requests.get(f'{base_url}{dairy}')
soup = BeautifulSoup(res.text, 'html.parser')
