from bs4 import BeautifulSoup
import requests
from csv import reader
from csv import writer

site = 'http://quotes.toscrape.com/'
response = requests.get(site)

print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.select('.col-md-8')
text

text2 = soup.select('.text')

list(text2)
type(text2[0])
dir(text2[0])
