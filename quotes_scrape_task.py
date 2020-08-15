
import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urljoin


rootpage = 'http://quotes.toscrape.com/'
result = requests.get(rootpage)
page = result.text
page

## Using bs4
soup = BeautifulSoup(page, 'html.parser')
quotes = soup.find_all('div', class_='quote')
len(quotes)
quotes[0]

|type(quotes)

quotes[0].find('div')


l = [1,2,3]
l+l

counter = 0
while counter<10:
    print(counter)
    counter+=1

while True:
    if counter<10:
        print(counter)
    else:
        break


l.append([4,5])

l






# ## Example on on quote
# quote = quotes[0]
# text = quote.find('span', class_='text').text
# print(text)
# author = quote.find('small', class_='author').text
# print(author)



scraped = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    scraped.append([text, author])

results_df = pd.DataFrame(scraped, columns=['quote','author'])
results_df.head()


# Find all links
soup.find_all("a")

# Look at single one
soup.find_all("a")[0]
soup.find_all("a")[0]['href']


# Finding certin links based on text
soup.find_all("a", text="world")  # text equals exactly
soup.find_all("a", text=lambda text: text and "w" in text)  # 'price' is inside the text


# Look at order number
pd.DataFrame(soup.find_all("a"))

## Looking at the page
soup.find_all("a")[42]
soup.find_all("a")[42].text
soup.find_all("a")[42].find('span').text


## Find next page
try:
    next_page = soup.find(class_ = 'next')
    next_page_url = next_page.find("a")['href']
except:
    return

urljoin(rootpage, next_page_url)

next_page = urljoin(rootpage, next_page_url)


def pull_quotes(page):
    result = requests.get(page)
    page = result.text
    page

    ## Using bs4
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    len(quotes)
    quotes[0]





from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/')
page = driver.page_source

## Click the next page
elem = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/nav/ul/li/a')
elem.click()






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
    author_links = []
    for quote in quotes:
        text = quote.find('span', class_ = 'text').text
        quote_list.append(text)
        author = quote.find('small', class_ = 'author').text
        author_list.append(author)
        author_link = quote.find_all('span')[1].find('a')['href']
        author_links.append(author_link)
    try:
        next_page = soup.find(class_ = 'next')
        next_page_url = next_page.find('a')['href']
    except:
        next_page_url = None
    return quote_list, author_list,author_links, next_page_url


#######################
# Loop all pages
#######################
quotes_all = []
authors_all = []
author_links_all = []
rootpage = 'http://quotes.toscrape.com'

# Initialize the first "Next page" as the rootpage
next_page = rootpage

for i in range(10):
    print('current_page:', next_page)
    # Run for current page - current next_page is rootpage
    quote_text, author_names, author_links, next_page_url = page_open(next_page)
    quotes_all = quotes_all + quote_text
    authors_all = authors_all + author_names
    author_links_all = author_links_all + author_links
    # Now we set the "next_page" with the next page
    next_page = urljoin(rootpage, next_page_url)

    print('\tquotes_all:',len(quotes_all))
    print('\tauthors_all:',len(authors_all))
    print('\tnext_page:', next_page)


dict(zip(authors_all,author_links_all))
pd.DataFrame(zip(authors_all,author_links_all))


all_results_df = pd.DataFrame(zip(authors_all,author_links_all,quotes_all), columns=['author','author_link','quote'])
all_results_df.head()

author_results_df = pd.DataFrame(zip(authors_all,author_links_all), columns=['author','author_link'])
author_results_df.head()

author_results_df.drop_duplicates()


## Write a function to find author details
len(authors_all)
len(set(authors_all))




# quotes_all = []
# authors_all = []
# rootpage = 'http://quotes.toscrape.com'
#
# # Initialize the firstscrape
# quote_text, author_names, next_page = page_open(rootpage)
#
# # Now run for the "pages"
# for i in range(2):
#     # Run for current page - current next_page is rootpage
#     quote_text, author_names, next_page_url = page_open(next_page)
#     quotes_all = quotes_all + quote_text
#     authors_all = authors_all + author_names
#     # Now we set the "next_page" with the next page
#     next_page = urljoin(rootpage, next_page_url)
#     print('next_page:', next_page)
