import requests
from selectolax.parser import HTMLParser
import re
import pandas as pd


domain = "http://books.toscrape.com/"
urls = [f"https://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 51)]


output = []
for url in urls:
    r = requests.get(url)
    tree = HTMLParser(r.text)

    div = tree.css("section > div")
    books = div[1].css("li > article")
    books = books[:-2]

    for book in books:
        temp_url = book.css_first("h3 > a").attributes.get("href")
        pattern = r"/([^_/]+)_\d+/index\.html"
        match = re.search(pattern, temp_url) if  temp_url else None
        title = match.group(1).replace("-", " ") if match else None
        book_url = domain + "catalogue/" + temp_url if temp_url else None

        price_div = book.css_first("div.product_price")
        price = price_div.css_first("p.price_color").text()
        stock = price_div.css_first("p.instock.availability > i").text()
        if stock and stock.strip() == "In stock":
            stock_availability = True
        else:
            stock_availability = False

        
        output.append({
            "title": title,
            "book_url": book_url,
            "price": price,
            "stock_availability": stock_availability,
        })

df = pd.DataFrame(output)
df.to_csv("test.csv", index=False)   
