# ------------------------------------------ myproject\myproject\middlewares.py ------------------------------------------
#-
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#-
from scrapy import signals
#-
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter                                   #panco: add stuff to the HTTP request and response
#-                                                                             #  eg.: add proxy to the request - using different IP address to by-pass restrictions on web scraping of the website
#-                                                                             #       post-processing on the return data of the HTTP response
class MyprojectSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
#-
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
#-
    def process_spider_input(self, response, spider):                          #panco: 6. process the response from downloader
        # Called for each response that goes through the spider
        # middleware and into the spider.
#-
        # Should return None or raise an exception.
        return None
#-
    def process_spider_output(self, response, result, spider):                 #panco: 7. output of spider callbacks - change/add/remove requests or items
        # Called with the results returned from the Spider, after              #       call errback instead of callback for some of the requests based on response content
        # it has processed the response.
#-
        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i
#-
    def process_spider_exception(self, response, exception, spider):           #panco: 6.1. handle spider exceptions           
        # Called when a spider or process_spider_input() method                         
        # (from other spider middleware) raises an exception.
#-
        # Should return either None or an iterable of Request or item objects.
        pass
#-
    def process_start_requests(self, start_requests, spider):                  #panco: 7.1. start a new requests to follow
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.
#-
        # Must return only requests (not items).
        for r in start_requests:
            yield r
#-
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
#-
#-
class MyprojectDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
#-
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
#-
    def process_request(self, request, spider):                                #panco: 4. process the HTTP request and pass request to downloader
        # Called for each request that goes through the downloader
        # middleware.
#-
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
#-
    def process_response(self, request, response, spider):                     #panco: 5. after downloader got the page and generated the response, middleware can process this response
        # Called with the response returned from the downloader.
#-
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
#-
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
#-
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
#-
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
