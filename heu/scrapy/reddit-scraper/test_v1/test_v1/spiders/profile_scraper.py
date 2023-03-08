import scrapy


class ProfileScraperSpider(scrapy.Spider):
    name = "profile_scraper"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://www.reddit.com/user/AceSenpai98/", "https://www.reddit.com/user/epiccool69/", "https://www.reddit.com/user/GeneralSpectatorTots/", "https://www.reddit.com/user/kyoto93/", "https://www.reddit.com/user/WSJ_Official/", "https://www.reddit.com/user/Timedoutsob/"]

    def parse(self, response):
        karma = response.css("span#profile--id-card--highlight-tooltip--karma::text").get()
        account_created = response.css("span#profile--id-card--highlight-tooltip--cakeday::text").get()
        bio = response.css("div.bVfceI5F_twrnRcVO1328::text").get()
        latest_link = response.css("div.y8HYJ-y_lTUHkQIc1mdCq._2INHSNB8V5eaWp4P0rY_mE > a::attr(href)").get()

        if latest_link == None:
            latest_link = ""
        else:
            latest_link = "https://www.reddit.com" + latest_link

        yield {
            "username": response.url.replace("https://www.reddit.com/user/", "").replace("/", ""),
            "karma": karma,
            "account_created": account_created,
            "bio": bio,
            "latest_activity_link": latest_link,
        }