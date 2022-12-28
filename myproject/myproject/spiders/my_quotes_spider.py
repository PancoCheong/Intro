# ------------------------------------------ myproject\myproject\spiders\my_quotes_spider.py ------------------------------------------
#-
import scrapy
from ..items import MyprojectItem                  # import the data model defined in items.py on parent folder

class MyQuoteSpider(scrapy.Spider):                # our class must inherit from Spider
#- variables
#  scrapy.Spider expects these two variables
    name = 'quotes'                                # name of our spider
    start_urls = ['http://quotes.toscrape.com'      
    ]                                              # list of URLs to scrap
#-
#- functions
    def parse(self, response):                           # response - the webpage source code
# #       title = response.css('title').extract()        # get <title>Quotes to Scrape</title>
#         title = response.css('title::text').extract()  # get the text from <title>Quotes to Scrape</title> using CSS selector
#         yield {'mytitletext' : title}                  # yield functions expects dictionary
#                                                        #     yield - like a return keyword of a function, commonly used in generator 
#                                                        #     Scrapy uses generator behind the scene
#- use data model
        items = MyprojectItem()                                  # initialize an object of MyprojectItem class
#-                                                               
#       all_div_quotes = response.css('div.quote')[0]            # [0] - get 1st record as a sample
        all_div_quotes = response.css('div.quote')               # get all quotes from <div class="quote"
#-
        for quote in all_div_quotes:                             # get one record at a time
            title = quote.css('span.text::text').extract()       # get the text from <span class="text" 
            author = quote.css('.author::text').extract()        # get the text from <small class="author" 
            tags = quote.css('.tag::text').extract()             # get the text from <a class="tag"

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items                                          # every yield of the data, it sends to pipeline

            # yield {
            #     'title' : title,
            #     'author' : author,
            #     'tags' : tags           
            # }

