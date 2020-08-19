

def add(a, b):
    '''
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    '''
    return a * b
print(add(4,5))


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

bio_name = soupb.find('h3', class_ = 'author-title')
bio_dob = soupb.find('span', class_ = 'author-born-date')
bio_loc = soupb.find('span', class_ = 'author-born-location')
bio_desc = soupb.find('div', class_ = 'author-description')
biopage = urljoin(rootpage,author_links_all[0])

name = bio_name.text
author_main_name.append(name)
dob = bio_dob.text
author_dob.append(dob)
loc = bio_loc.text
author_loc.append(loc)
info = bio_desc.text
author_info.append(info)
