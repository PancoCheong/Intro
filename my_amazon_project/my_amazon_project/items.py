# ------------------------------------------ my_amazon_project\my_amazon_project\items.py ------------------------------------------
# -
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#-
import scrapy
#-
#-
class MyAmazonProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    book_image_link = scrapy.Field()
