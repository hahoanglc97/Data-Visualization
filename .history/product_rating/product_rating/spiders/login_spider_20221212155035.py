from scrapy import Spider
from scrapy.http import FormRequest


class LoginSpider(Spider):
    name = 'simple_login'

    def start_requests(self):
        login_url = 'https://member.lazada.vn/user/login'
        return FormRequest(login_url,
                            formdata={'loginName': '0836370836', 'password': 'Hahoanglc97'},
                            callback=self.start_scraping)

    def start_scraping(self, response):
        ## Insert code to start scraping pages once logged in
        pass