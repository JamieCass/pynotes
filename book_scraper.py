import scrapy

# to run this you would do it in ther terminal like this...

# scrapy runspider -o 'books.csv' (the name of the file you want to save the info to) 'book_scraper.py' (the name of the file scrapy is in)

#scrapy uses css syntax so we need to learn that..

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):# same as soup.select but written in srapy syntax
            yield {
                'price': article.css('.price_color::text').extract_first(), # this will extract the text (like soup.get_text())
                'title': article.css('h3 > a::attr(title)').extract_first()
            }
            # this is how you will go through all the pages and get the price and title from every book.
            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)
