import scrapy


class QuotescraperSpider(scrapy.Spider):
    name = "quotescraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        text = response.css('div.quote span.text::text').getall()
        author = response.css('div.quote small.author::text').getall()

        for i in range(len(text)):
            yield {"text": text[i], "author": author[i]}
