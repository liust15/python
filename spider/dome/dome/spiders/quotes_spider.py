import scrapy
class QueteSpider(scrapy.Spider):
    name="quotes"
    def start_requests(self):
        urls =[
            'http://www.toutiao.com/a6481175514097648141/',
           ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)