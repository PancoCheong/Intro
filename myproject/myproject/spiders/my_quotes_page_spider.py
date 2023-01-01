# ------------------------------------------ myproject\myproject\spiders\my_quotes_page_spider.py ------------------------------------------
# -
import scrapy
# import the data model defined in items.py on parent folder
from ..items import MyprojectItem


# our class must inherit from Spider
class MyQuoteSpider(scrapy.Spider):
#- variables
#  scrapy.Spider expects these two variables
    name = 'quotes_page'                                # name of our spider, pagination
    start_urls =    ['https://quotes.toscrape.com/page/1/'
                    ]                                              # list of URLs to scrap
#- class variable
    page_number = 2
# -
#- functions

    def parse(self, response):                           # response - the webpage source code

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

# - follow next page link and extract content from it
#         next_page = response.css('li.next a::attr(href)').get()c
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)
        next_page = 'https://quotes.toscrape.com/page/' + str(MyQuoteSpider.page_number) + '/'
        print(next_page)                #show the progress
# -
        if MyQuoteSpider.page_number < 11:
            MyQuoteSpider.page_number += 1
            # go to next page and use this parse() to extract content
            yield response.follow(next_page, callback=self.parse)
