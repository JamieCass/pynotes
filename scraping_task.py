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

######################################################################################################################################################

##################################################
# ALL PAGE SCRAPE
##################################################
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

######################################################################################################################################################

##################################################
# AUTHOR BIO
##################################################
author_links_all
len(author_links_all)

def bio_open(site):
    '''
    request the site
    parse into bs
    find author D.O.B, birth location and some details about them.
    '''
    bio_r = requests.get(site)
    soupb = BeautifulSoup(bio_r.text, 'html.parser')
    bio_name = soupb.find('h3', class_ = 'author-title')
    bio_dob = soupb.find('span', class_ = 'author-born-date')
    bio_loc = soupb.find('span', class_ = 'author-born-location')
    bio_desc = soupb.find('div', class_ = 'author-description')
    author_main_name = []
    author_dob = []
    author_loc = []
    author_info = []
    name = bio_name.text
    author_main_name.append(name)
    dob = bio_dob.text
    author_dob.append(dob)
    loc = bio_loc.text
    author_loc.append(loc)
    info = bio_desc.text
    author_info.append(info)

    return author_main_name, author_dob, author_loc, author_info


#######################
# Loop all author pages
#######################
biopage = urljoin(rootpage,author_links_all[0])
next_page1 = biopage
all_author_main_name = []
all_author_dob = []
all_author_loc = []
all_author_info = []


for i in set(author_links_all):
    print('current_page:', next_page1)
    author_main_name, author_dob, author_loc, author_info = bio_open(next_page1)
    all_author_main_name = all_author_main_name + author_main_name
    all_author_dob = all_author_dob + author_dob
    all_author_loc = all_author_loc + author_loc
    all_author_info = all_author_info + author_info
    next_page1 = urljoin(biopage, i)
    # print('\tauthor_main_name:',len(all_author_main_name))
    # print('\tall_author_dob:',len(all_author_dob))
    # print('\tall_author_loc:',len(all_author_loc))
    # print('\tall_author_info:',len(all_author_info))
all_author_dob
all_author_loc

######################################################################################################################################################
#######################
# Guessing Game Code
#######################
import random

q1 = quotes_all[1]

quote_index = quotes_all.index(q1)
quote_index
authors_all[quote_index]
correct_answer = authors_all[quote_index]
correct_answer
hint = [x[0] for x in correct_answer.split()]

print(hint)
def question():
    '''
    Function that allows user to play a guessing game, guessing who wrote a quote.
    User gets 4 tries, after each wrong answer they get a clue to help them.
    After user has no more guesses they get the answer and option to play again.
    '''
    ##############################################
    # Set up of the hints and where to get everything from..
    tries = 4
    Q1 = quotes_all[0]
    # Q1 = random.choice(quotes_all)
    quote_index = quotes_all.index(Q1)
    correct_answer = authors_all[quote_index]
    name_hint = [x[0] for x in correct_answer.split()]

    ##############################################
    # Set up the scraping part..
    rootpage = 'http://quotes.toscrape.com'
    biopage = urljoin(rootpage,author_links_all[quote_index])
    r = requests.get(biopage)
    soup = BeautifulSoup(r.text, 'html.parser')

    ##############################################
    # Set the scraping of the DOB and LOC of the authors for hints..
    dob = soup.find('span', class_ = 'author-born-date')
    loc = soup.find('span', class_ = 'author-born-location')

    ##############################################
    # Print statements and what to do when they get it wrong or right..
    print(Q1)
    answer = input('Can you guess who said the quote?')

    while tries > 0:
        if answer.lower() != correct_answer.lower() and tries >3:
            tries -= 1
            print(f'WRONG!. Tries remaining {tries}',)
            print(f'\tHINT. This author was born: {dob.text}')
            answer = input('2nd try..')
        elif answer.lower() != correct_answer.lower() and tries >2:
            tries -= 1
            print(f'Still WRONG!. Tries remaining {tries}')
            print(f'\tHINT. This author was born {loc.text}')
            answer = input('3rd try..')
        elif answer.lower() != correct_answer.lower() and tries >1:
            tries -= 1
            print(f'Still WRONG!. Tries remaining {tries}')
            print(f'\tLAST HINT... The first letters of the authors name are: {name_hint}')
            answer = input('Last try..')
        elif answer.lower() != correct_answer.lower():
            print(f'WRONGGGGG!!! \n\tThe correct answer was: {correct_answer}')
        else:
            return 'WELL DONE'

    print(f'WRONGGGGG!!! \n\tThe correct answer was: {correct_answer}')

question()
