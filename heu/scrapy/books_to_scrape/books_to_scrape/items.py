# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
import re
from word2number import w2n

def remove_currency(text):
    return float(text.replace("£", ""))


def url2title(url):
    temp = url.replace("/index.html", "").replace("-", " ")
    return re.sub(r'_\d+', '', temp)


def urljoin(url):
    return "https://books.toscrape.com/catalogue/" + url


def filter_stocknum(stock_num):
    return int(re.sub(r'\D', '', stock_num))


def filter_rating(rating):
    word_rating = rating.split()[1]
    return w2n.word_to_num(word_rating.lower())


class BooksToScrapeItem(scrapy.Item):
    default_output_processor = TakeFirst()
    # define the fields for your item here like:
    title = scrapy.Field(input_processor=MapCompose(url2title))
    url = scrapy.Field(input_processor=MapCompose(urljoin))
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency))
    stock_num = scrapy.Field(input_processor=MapCompose(filter_stocknum))
    description = scrapy.Field(input_processor=MapCompose(remove_tags))
    upc = scrapy.Field(input_processor=MapCompose(remove_tags))
    rating = scrapy.Field(input_processor=MapCompose(filter_rating))
