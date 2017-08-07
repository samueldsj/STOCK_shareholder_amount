# -*- coding: utf-8 -*-

# Scrapy settings for xqgdhs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xqgdhs'

SPIDER_MODULES = ['xqgdhs.spiders']
NEWSPIDER_MODULE = 'xqgdhs.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xqgdhs (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   #'Accept-Language': 'en',
   'Host':'xueqiu.com',
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language':'zh-CN,zh;q=0.8',
   'Accept-Encoding':'gzip, deflate, br',
   'cookie':'Hm_lvt_1db88642e346389874251b5a1eded6e3=1498786030,1498807924,1499040372,1500005029; device_id=ee5e75e0fdf0bad5a3e64b518fa09b7d; aliyungf_tc=AQAAANmFGEI99QwA2xBGfa6WDyyBx50T; xq_a_token=dab8000cc046577e0ed41bcd7f3929995b5fb44e; xq_a_token.sig=dR_XY4cJjuYM6ujKxH735NKcOpw; xq_r_token=d15cbd95276720522d8cb71c74a9d13438b23680; xq_r_token.sig=8d4jOYdZXEWqSBXOB9N5KuMMZq8; u=3827818735; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1500005170; s=es12g4m0ey; xqat=dab8000cc046577e0ed41bcd7f3929995b5fb44e; xq_token_expire=Tue%20Aug%2008%202017%2012%3A05%3A57%20GMT%2B0800%20(CST); xq_is_login=1; bid=73f873c23331f78120dfffc822ba1868_j53ccbzo',
   'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0',
   'Connection':'keep-alive',
   'Upgrade-Insecure-Requests':'1',
   'Cache-Contrl':'max-age=0'
}



# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xqgdhs.middlewares.XqgdhsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'xqgdhs.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xqgdhs.pipelines.XqgdhsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
