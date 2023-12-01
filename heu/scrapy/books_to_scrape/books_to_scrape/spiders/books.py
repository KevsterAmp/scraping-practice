import scrapy
import re
from ..items import BooksToScrapeItem
from scrapy.loader import ItemLoader


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        for book in response.css("ol.row > li > article.product_pod"):
            il = ItemLoader(item=BooksToScrapeItem(), selector=book)

            il.add_css("url", "div.image_container > a::attr(href)")
            il.add_css("title", "div.image_container > a::attr(href)")
            il.add_css("price", "div.product_price > p.price_color")

            book_item = il.load_item()
            # scrapy Request to the url in the itemloader
            yield scrapy.Request(str(book_item['url'][0]), callback=self.parse_book_details, meta={'book_item': book_item})

        next_page = response.css("ul.pager > li.next > a::attr(href)").get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_book_details(self, response):
        il = ItemLoader(item=response.meta['book_item'], selector=response)

        il.add_css("stock_num", "div.product_main > p.instock.availability")
        # il.add_css("description", "article.product_page > p")
        il.add_css("upc", "table > tr:nth-child(1) > td")
        il.add_css("rating", "div.product_main p.star-rating::attr(class)")

        yield il.load_item()

        
