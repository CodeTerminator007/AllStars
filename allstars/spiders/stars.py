import scrapy
import json
from scrapy_splash import SplashRequest

class StarsSpider(scrapy.Spider):
    name = 'stars'
    allowed_domains = ['www.pickstar.com.au/our-stars']
    script = '''
    function main(splash, args)
        splash:set_custom_headers(headers)
        assert(splash:go(args.url))
        assert(splash:wait(1))
        splash:set_viewport_full()
        return {
            html = splash:html()
        }
    end
    '''
    def start_requests(self):
        yield SplashRequest(url = "https://pickstar.com.au/api/our-stars?search_terms=&page=1" , callback = self.parse , endpoint ="execute" , args={
            'lua_source' : self.script
            })

    def parse(self, response):
        pass