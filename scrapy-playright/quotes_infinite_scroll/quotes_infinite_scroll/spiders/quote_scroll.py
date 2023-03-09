import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.selector import Selector

class QuoteScrollSpider(scrapy.Spider):
    name = "quote_scroll"
    
    def start_requests(self):
        yield scrapy.Request(
            url = "https://httpbin.org/get", 
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "div.quote")
                    ]   
                },
            errback=self.close_page
        )

    async def parse(self, response):
        page = response.meta['playwright_page']
        last_height = await page.evaluate("return document.body.scrollHeight")
        while True:
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
            new_height = await page.evaluate("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        html = await page.content()
        await page.close()

        website = Selector(text=html)
        quotes = website.css("div.quote > span.text::text").getall()

        for quote in quotes:
            yield {"quote": quote}

    async def close_page(self, error):
        page = error.request.meta['playwright_page']
        await page.close()
