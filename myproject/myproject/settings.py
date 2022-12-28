# ------------------------------------------ myproject\myproject\settings.py ------------------------------------------
#
# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#-
BOT_NAME = 'myproject'                                                         #panco: web scrapper is considered as bot, which automates the action of web scraping (aka. crawling)
#-
SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'
#-

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myproject (+http://www.yourdomain.com)'                         #panco: identify the application that sends the HTTP request. Eg. Identify yourself by your domain name (optional)
#-                                                                             #       many websites have restrictions on web scraping, we may use USER_AGENT to by-pass them
# Obey robots.txt rules
ROBOTSTXT_OBEY = True                                                          #panco: if True, follows the rules stated in the robots.txt file and does not crawl those disallowed contents
#-
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32                                                      #panco: how many request to crawl the website simultaneously (default=16)
#-                                                                             #       don't set too high as you may kill the web server or the web server may block your request 
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
#-
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
#-
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
#-
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
#-
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myproject.middlewares.MyprojectSpiderMiddleware': 543,
#}
#-
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.MyprojectDownloaderMiddleware': 543,
#}
#-
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
#-
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#-
#- 300 is priority, the lower the number, the higher the priority
#-     we can add more pipeline in ITEM_PIPELINES with different priority number
ITEM_PIPELINES = {
   'myproject.pipelines.MyprojectPipeline': 300,
}
#-
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True                                                   #panco: help to prevent overload the web server
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
#-
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#-
# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
