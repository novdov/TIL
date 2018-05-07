import scrapy

from gb_crawler.items import GbCrawlerItem

class GBSpider(scrapy.Spider):
    name = "GmarketBestsellers"
    allow_domain = ["gmarket.co.kr"]
    # 크롤링의 시작 URL
    start_urls = [
        "http://corners.gmarket.co.kr/Bestsellers"
    ]

    # link 리스트를 가져옴
    def parse(self, response):
        bestsellers = response.xpath('//*[@id="gBestWrap"]/div/div[3]/div[2]/ul/li')[:10]
        for bestseller in bestsellers:
            link = bestseller.xpath('./a/@href').extract()[0]
            print(link)
            yield scrapy.Request(link, callback=self.parse_page_contents)

    # 각페이지의 link로 접속하여 데이터를 가져옴
    def parse_page_contents(self, response):
        item = GbCrawlerItem()
        item["title"] = response.xpath('//*[@id="itemcase_basic"]/h1/text()')[0].extract().strip()
        item["s_price"] = response.xpath('//*[@id="itemcase_basic"]/p/span/strong/text()')[0].extract().replace(",","")
        item["o_price"] = response.xpath('//*[@id="itemcase_basic"]/p/span/span/text()')[0].extract().replace(",","")
        item["discount_rate"] = str(round((1 - int(item["s_price"]) / int(item["o_price"])) * 100, 2)) + "%"
        yield item
