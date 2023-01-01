# ------------------------------------------ my_amazon_project\my_amazon_project\spiders\items.py ------------------------------------------
# -
import scrapy
from ..items import MyAmazonProjectItem
from scrapy.utils.response import open_in_browser   # open the response in Web Browser

#-
class MyAmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1672480014&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
        ]
#-
#- class variable - next page number
    page_number = 2

    def parse(self, response):
        #-
        open_in_browser(response)
        #- init the object
        items = MyAmazonProjectItem()
#-
        #- .extract() == getall()
        book_name = response.css('.a-size-medium::text').extract()
        #- because multiple values, use one more css()
        book_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
        book_price = response.css('.s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole').css('::text').extract()
        book_image_link = response.css('.s-image-fixed-height .s-image').css('::attr(src)').extract()


#-
        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['book_image_link'] = book_image_link
#-
        yield items        

        #  yield response.follow(next_page, callback=self.parse)
        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(MyAmazonSpiderSpider.page_number) + '&qid=1672564010&rnid=1250225011&ref=sr_pg_' + str(MyAmazonSpiderSpider.page_number)
        print(next_page)                #show the progress
# -
        if MyAmazonSpiderSpider.page_number < 76:
            MyAmazonSpiderSpider.page_number += 1
            # go to next page and use this parse() to extract content
            yield response.follow(next_page, callback=self.parse)
