# ------------------------------------------ myproject\myproject\items.py ------------------------------------------
#-
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#-
import scrapy
#-
#-
class MyprojectItem(scrapy.Item):                                              #panco: define the data fields for your items
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
