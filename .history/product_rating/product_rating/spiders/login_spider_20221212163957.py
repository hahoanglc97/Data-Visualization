from scrapy import Spider
from scrapy.http import FormRequest
import scrapy
from scrapy.shell import inspect_response
from http import cookies

class LoginSpider(Spider):
    name = 'login_spider'

    def start_requests(self):
        login_url = 'https://member.lazada.vn/user/login'
        yield scrapy.Request(login_url, callback=self.login)
    
    def login(self, response):
        yield FormRequest.from_response(response,
                                         formdata={'password': '0836370836',
                                                   'username': 'Hahoanglc97'},
                                         callback=self.start_scraping)

    def start_scraping(self, response):
        # inspect_response(response, self)
        print(response.text)
        pass

