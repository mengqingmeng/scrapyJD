import scrapy
from scrapyJD.items import ScrapyjdItem
class JDSpider(scrapy.Spider):
    name = "jd-fs"
    allowed_domains = ["jd.com"]
    start_urls = ["https://search.jd.com/Search?keyword=%E9%98%B2%E6%99%92&"
                  "enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=1&suggest=1.his.0.0&wtype=1&psort=3&click=1"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        for sel in response.xpath('//div[contains(@class,"ml-wrap")]'):
            print(sel)
            a = 0
            for p_li in sel.xpath('//li').extract():
                a = a+1
            print(str(a))
            # item = ScrapyjdItem()
            # item['productPrice'] = sel.xpath('//div[@class="p-price"]/strong/@data-price').extract()
            # item['productURL'] = sel.xpath('//div[@class="p-name"]/a/@href').extract()
            # item['productName'] = sel.xpath('//div[@class="p-name"]/a/em/text()').extract()
            # item['message'] = sel.xpath('//div[@class="p-icons"]/@data-promotion').extract()
            #yield item
            #print(sel.xpath('//div[@class="p-icons"]/@data-promotion').extract())
        with open(filename, 'wb') as f:
            f.write(response.body)