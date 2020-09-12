# This is how the Tutor did the scraping task.
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader

base_url = 'http://quotes.toscrape.com'

############################## initiate the scrape (only used once) ##############################
all_quotes = []
url = '/page/1'

while url:
    res = requests.get(f'{base_url}{url}')
    print(f'Now scraping {base_use}{url}...')
    soup = BeautifulSoup(rex.text, 'html.parser')
    quotes = soup.find_all(class_='quote')

    for quote in quotes:
        all_quotes.append({
            'text':quote.fund(class_='text').get_text(),
            'author':quote.find(class_='author').get_text(),
            'bio-link':quote.find('a')['href']
        })
    ############### go to the next page ###############
    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None

############################## open the csv with all quotes in ##############################
def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes
read_quotes('quotes.csv')

############################## create game function ##############################
def start_game(quotes):
    quote = choice(quotes)
    print(quote['text'])
    remaining_guesses = 4
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f'Who said this quote? Guesses remaining: {remaining_guesses}\n')
        if guess.lower() == quote["author"].lower():
            print('WELL DONE, YOU GOT IT RIGHT')
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_place = soup.find(class_='author-born-location').get_text()
            print(f'Heres a hint: The author was born on {birth_date} {birth_place}')
        elif remaining_guesses == 2:
            print(f"Here's a hint: The authors first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(' ')[1][0]
            print(f"Here's a hint: The authors last name starts with {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

############################## create the 'play again' option ##############################
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input('Would you like to play again (y/n)?')
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print('Ok goodbye..')

quotes = read_quotes('quotes.csv')
start_game(quotes)
