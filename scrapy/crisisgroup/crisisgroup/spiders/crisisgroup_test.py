import scrapy


class CrisisgroupTestSpider(scrapy.Spider):
    name = "crisisgroup-test"
    allowed_domains = ["www.crisisgroup.org"]
    start_urls = ["https://www.crisisgroup.org/latest-updates/reports-and-briefings?page="+ str(i) for i in range(1, 11)]

    def parse(self, response):
        links = response.css('h4.c-news-listing__title a::attr(href)').getall()
        for link in links:

            yield {
                'source': response.url,
                'link': 'https://www.crisisgroup.org/' + link
            }