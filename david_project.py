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
import matplotlib.pyplot as plt
import seaborn as sns

############################## all book urls ##############################
#
# base_url = 'http://books.toscrape.com/catalogue/'
# url = 'page-1.html'
# all_books = []
#
# while url:
#     res = requests.get(f'{base_url}{url}')
#     soup = BeautifulSoup(res.text, 'html.parser')
#
#     ############### list of the book pages ###############
#
#     books = soup.find_all('article')
#
#     for book in books:
#         book_link = book.find('a')['href']
#         all_books.append(book_link)
#
#
#     ############### go to the next page ###############
#     next_btn = soup.find(class_='next')
#     url = next_btn.find('a')['href'] if next_btn else None

len(all_books)
all_books[161]

############################## loop all book urls ##############################

#
# def book_page_open(site):
#     '''
#     request the site
#     parse into bs
#     find title, price, rating, upc, stock and desription
#     '''
#
#
#     b_page = requests.get(site)
#     bsoup = BeautifulSoup(b_page.text, 'html.parser')
#
#     title = bsoup.find('h1').text
#
#
#     prod_price = bsoup.find(class_='price_color').text
#     price = float(prod_price.replace('£','').replace('Â',''))
#
#
#     ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
#     rate = bsoup.select('.star-rating')[0]
#     rating_word = rate.get_attribute_list('class')[-1]
#     rating = ratings[rating_word]
#
#
#     table = bsoup.find(class_= 'table table-striped')
#     upc = table.find('td').get_text()
#
#     prod_stock = bsoup.find(class_='instock availability').text
#     # prod_stock = prod_stock.replace('\n', '').replace('  ','').replace('(','').replace(')','').split('\n')
#     stock = prod_stock[prod_stock.find('(')+1:prod_stock.find('available')-1]
#
#     desc = bsoup.find(class_='product_page').find_all('p')
#     desc = [x for x in desc if x.attrs=={}]
#     if len(desc)==0:
#         desc = 'No review'
#     else:
#         desc = desc[0].text
#
#     src = bsoup.find('img')
#     img_src = next(iter(src.attrs.values())).replace('../..','')
#
#     cat = bsoup.find_all(class_='page_inner')
#     for x in cat:
#         bread = x.find(class_='breadcrumb')
#     category = bread.find_all('li')[2].text.replace('\n','')
#
#     # sleep(0.5)
#
#     return title, price, rating, upc, stock, desc, img_src, category
#
#
# all_book_info = []
#
# for i in all_books:
#     print('current_page:', base_url,i)
#     title, price, rating, upc, stock, desc, img_src, category  = book_page_open(urljoin(base_url, i))
#     all_book_info.append([upc, title, price, rating, stock, img_src, desc, category])


######################################################## TEST ########################################################


main_df = pd.read_csv('/Users/jamie/Coding/pynotes/book_main.csv')
main_df = main_df.drop(main_df.columns[0], axis=1)
main_df

# top 5 with a rating of 5
main_df['Title'][main_df['Stock'] == 1]
# top 5 with all the information
main_df['Price'][main_df['Rating'] == 5].mean()

main_df[main_df['Rating'] == 5]

main_df.sort_values('Stock').tail(20)



sns.regplot(x="Rating", y="Price", data=main_df)

sns.boxplot(x="Rating", y="Price", data=main_df)

rating_price_df = main_df[['Rating', 'Price']]
rating_price_df.groupby('Rating', as_index=False).mean()

rating_cat_price = main_df[['Rating', 'Category', 'Price']]
cat_mean_df = rating_cat_price.groupby('Category', as_index=True).mean()

################### AVG PRICE AND RATING PER CATEGORY ###################
cat_mean_df

sns.regplot(x='Rating', y='Price', data=cat_mean_df)

# Line graph to show average rating and prices
sns.lineplot(x='Rating', y='Price', data=cat_mean_df)

# graph showing average price and rating for each category
cat_mean_df.plot(xlabel='Category',title='Category vs Price & Rating', figsize=(20,10), kind='bar')


set(main_df['Category'])


cat_mean_df[(cat_mean_df['Rating']>=3)]

main_df[((main_df['Rating'] >= 4) & (main_df['Price'] > 20.00))]


# img_df = pd.read_csv('/Users/jamie/Coding/pynotes/book_img.csv')
# img_df
# desc_df = pd.read_csv('/Users/jamie/Coding/pynotes/book_desc.csv')
# desc_df = desc_df.drop(desc_df.columns[0], axis=1)
# desc_df
