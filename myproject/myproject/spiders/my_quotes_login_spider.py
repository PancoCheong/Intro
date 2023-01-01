# ------------------------------------------ myproject\myproject\spiders\my_quotes_login_spider.py ------------------------------------------
# -
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser   # open the response in Web Browser
#-
# import the data model defined in items.py on parent folder
from ..items import MyprojectItem


# our class must inherit from Spider
class MyQuoteSpider(scrapy.Spider):
#- variables
#  scrapy.Spider expects these two variables
    name = 'quotes_login'                                # name of our spider, pagination
    start_urls =    ['https://quotes.toscrape.com/login'
                    ]                                              # list of URLs to scrap
#- functions
    def parse(self, response):                           # response - the webpage source code
        token = response.css('form input::attr(value)').extract_first()
        print('csrf token:' + token)
    #-
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username': 'abc@xyz.net',
            'password': '1234'
        }, callback = self.start_scraping)      # what to do after the login
#-
#- scraping method
    def start_scraping(self, response):
        open_in_browser(response)
#-
        items = MyprojectItem()
# -
#       all_div_quotes = response.css('div.quote')[0]            # [0] - get 1st record as a sample
        # get all quotes from <div class="quote"
        all_div_quotes = response.css('div.quote')
# -
        for quote in all_div_quotes:                             # get one record at a time
            # get the text from <span class="text"
            title = quote.css('span.text::text').extract()
            # get the text from <small class="author"
            author = quote.css('.author::text').extract()
            # get the text from <a class="tag"
            tags = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            # every yield of the data, it sends to pipeline
            yield items
#-    
    # - follow next page link and extract content from it
        next_page = response.css('li.next a::attr(href)').get()
        print(next_page)  # show the progress
# -
        if next_page is not None:
            # go to next page and use this start_scraping() to extract content
            # just like a recursive method
            yield response.follow(next_page, callback=self.start_scraping)
