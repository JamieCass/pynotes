import scrapy

# to run this you would do it in ther terminal like this...

# scrapy runspider -o books.csv (the name of the file you want to save the info to) book_scraper.py (the name of the file scrapy is in)


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):# same as soup.select but written in srapy syntax
            yield {
                'price': article.css('.price_color::text')
            }
