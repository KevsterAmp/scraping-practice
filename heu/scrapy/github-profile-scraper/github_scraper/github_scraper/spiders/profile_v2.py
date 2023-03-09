import scrapy
import pandas as pd

class GithubProfieScraperSpider(scrapy.Spider):
    name = "github_profile_scraper"
    allowed_domains = ["github.com"]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        # github_users = ["PaullyMac", "marcoxmediran", "yam-1111", "kisuuuuu", "notJevan", "fglopezjr", "markmcrg", "jrzvnn", "znarfm", "elexielle", "Pipluppp", "ron-ligsay"]
        # github_users_url = ["http://github.com/"+ user for user in github_users]
        # self.start_urls = github_users_url
        # self.start_urls = ["http://github.com/"+ user for user in self.df['user'].tolist()]
        self.df = pd.read_csv("github_users.csv")
        self.start_urls = self.df["user_url"].tolist()
                
    def parse(self, response):
        fullname = response.css("span.vcard-fullname::text").get().strip()
        username = response.css("span.vcard-username::text").get().strip()
        contributions = response.css("div.position-relative > h2::text").get()
        bio = "".join(response.css("div.user-profile-bio > div > *::text, div.user-profile-bio > div::text ").getall()).strip()
        followwers = response.css("a[href$='followers'] > span::text").get()
        following = response.css("a[href$='following'] > span::text").get()

        if contributions is not None:
            contributions = contributions.split()[0]

        yield {
            "fullname": fullname,
            "username": username,
            "contributions": contributions,
            "bio": bio,
            "followers": followwers,
            "following": following
        }