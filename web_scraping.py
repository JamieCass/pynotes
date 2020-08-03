#######################################################################
# Web scraping with Beautiful Soup
#######################################################################

##########################################   OBJECTIVES   ##########################################

# Define what web scraping is and the issues surrounding it
# Use the requests and BeautifulSoup modules to parse HTML
# Explain some common problems with web scraping
# Explore other tools that can interact with web pages

# Web scraping involves programatically grabbing data from a web page
# Three steps: Dowload, extract data, PROFIT!(do something with it)

##########################################   WHY SCRAPE   ##########################################

# Theres data on a site that you want to store or analyze
# You cant get by other means (e.g an API)
# You want to programatically grab the data (instead of lots of manual copying/pasting)

##########################################   IS SCRAPING OK   ##########################################

# Some websites dont want you to scrape them
# Best practice: consult the robots.txt file (will show you what the site would prefer you not to scrape)
# If youre making a lot of requests, time them out
# If youre too aggressive, your IP can be blocked

# e.g for robots.txt file (www.imdb.com/robots.txt)





##########################################   BeautifulSoup   ##########################################

# BeautifulSoup lets us navigate through HTML with Python
# BeautifulSoup does NOT download HTML - for this, we need the requests module


# ---------- HTML SLECTORS  ----------
# BeautifulSoup(html_string, 'html.parser') - parse HTML
# Once parsed, there are several ways to navagate:
#   - By Tag Name
#   - Using 'find' - returns on matching tag
#   - Using 'find_all' - returns a list of matching tags
# if you want to find by 'class' you need to put 'class_ ='

# ---------- CSS SLECTORS  ----------
# 'select' - returns a list of elements matching a CSS selector
# Selector Cheatsheet:
# - Select by id of foo: '#foo'
# - Select by class of bar: '.bar'
# Select children: 'div > p'
# Select decendents: 'div p'

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
c = soup.find_all(class_ = 'special') # this will print out all classes that are called 'special'
i = soup.find(id = 'first') # this will print out everything in <div id = 'first'>
css = soup.select('#first') # will give you the same result (in a list) as i.
d = soup.select("[data-example]")
# d = soup.find_all(attrs={'data-example': 'yes'}) # above code could of been written like this, but its not as nice!
print(d)
css
i

# ----------  SELECTING ELEMENTS BY ATTRIBUTE  ----------

# find an element with an id of foo
soup.find(id = 'foo')
soup.select('#foo')[0]

# find all elements with a class of bar
# careful! 'class' is a reserved word in python
soup.find_all(class_ = 'bar')
soup.select('.bar')

# find all elements with a data attribute of 'baz'
# using the general attrs kwarg
soup.find_all(attrs{'data-baz' = True})
soup.select('[data-baz]')


##########################################   ACCESSING DATA with BeautifulSoup   ##########################################

# ----------  ACCESSING DATA in ELEMENTS  ----------

# 'get_text' - access the inner text in an element
# 'name' - tag name
# 'attrs' - dictionary of attributes
# You can also access attribute values using brackets

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
el = soup.select('.special')[0]
el.get_text()  # this will show just the text from the 'special' class

for le in soup.select('.special'):
    print('This is the text: \n', le.get_text(), '\n')
    print('This is the name: \n', le.name, '\n')
    print('This is a dictionary of attributes: \n', le.attrs['class'], '\n')

attr = soup.find('h3')['data-example'] # find the h3 and what its called
attr
divv = soup.find('div')['id'] # find the first div and get the id name
divv

##########################################   FIRST SCRAPING PROGRAM   ##########################################

site = 'https://www.rithmschool.com/blog'
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(site)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')
print(articles)

with open('blog_data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

    for article in articles:
        a_tag = article.find('a') # save all the a tags to a variable
        title = a_tag.get_text() # we can use the a tag variable to call get_text
        url = a_tag['href'] # save all the urls from the a_tag we called
        date = article.find('time')['datetime']
        csv_writer.writerow([title, url, date])
a_tag
title
url
