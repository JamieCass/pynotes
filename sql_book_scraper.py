import sqlite3
import requests
from bs4 import BeautifulSoup

history_books = 'http://books.toscrape.com/catalogue/category/books/history_32/index.html')



def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article')
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    print(all_books)

# save all books to database.. (will add more notes at a later date)
def save_books(all_books):
	connection = sqlite3.connect("books.db")
	c = connection.cursor()
	c.execute('''CREATE TABLE books
		(title TEXT,price REAL,rating INTEGER)''')
	c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
	connection.commit()
	connection.close()

# get the title for all the books
def get_title(book):
    return book.find('h3').find('a')['title']

# get the price for all the books
def get_price(book):
    price = book.select('.price_color')[0].get_text()
    #convert prices into a float and get rind of the currency symbol
    return float(price.replace('£','').replace('Â',''))

# get the ratings for all the books
def get_rating(book):
    #set string rating to be integers
    ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    #get all the star ratings for each book
    paragraph = book.select('.star-rating')[0]
    word = paragraph.get_attribute_list('class')[-1]
    return ratings[word]



# Extract data we want

# Save data to database
