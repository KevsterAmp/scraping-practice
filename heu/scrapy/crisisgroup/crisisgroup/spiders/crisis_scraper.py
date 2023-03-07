import scrapy


class CrisisScraperSpider(scrapy.Spider):
    name = "crisis_scraper"
    allowed_domains = ["www.crisisgroup.org"]
    start_urls = ["https://www.crisisgroup.org/latest-updates?page=" + str(i) for i in range(644)]
    # start_urls = ["https://www.crisisgroup.org/latest-updates?page=1"]
         
    def parse(self, response):
        divs = response.css("div.c-news-listing__content")
        for div in divs:
            meta = div.css("div.c-news-listing__meta")
            topic = meta.css("a:nth-child(1)::attr(title)").get()
            region = meta.css("a:nth-child(2)::text").get()
            time = meta.css("time::text").get()

            h4 = div.css("h4.c-news-listing__title")
            title = h4.css("a::text").get()
            url = h4.css("a::attr(href)").get() 

            yield {
                "source": response.url,
                "url": "https://www.crisisgroup.org"+ url,
                "topic": topic,
                "region": region,
                "title": title,
                "date_published": time,
            }

        # # topic = response.css('div.c-news-listing__meta > a:nth-child(1)::attr(title)').extract()
        # # region = response.css('div.c-news-listing__meta > a:nth-child(2)::text').extract()
        # # title = response.css('h4.c-news-listing__title > a::text').extract()
        # # url = response.css("h4.c-news-listing__title > a::attr(href)").extract()
        # # date = response.css("div.c-news-listing__meta > time::text").extract()
                                 
        # for i in range(len(topic)):
        #     yield {
        #         "topic": topic[i],
        #         "region": region[i],
        #         "title": title[i],
        #         "url": url[i],
        #         "date": date[i],
        #         }