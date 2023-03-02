#hfr.org

#In scraping titles
response.css('h3.media-block__title a::attr(href)').getall()

#usip.org
#scraping links
response.css('h3.summary__heading a::attr(href)').getall()

#scraping articles
#title
response.css('header.page__header h1::text').get()

#text
response.css('section.wysiwyg *::text').getall()

propublica.org
scraping links
response.css('h2.hed a::attr(href)').getall()

scrpaing articles
author
response.css('div.metadata p  a::text').getall()

title 
response.css('h1.hed::text').get()

article 
response.css('div.article-body p::text, div.article-body  a::text').getall()