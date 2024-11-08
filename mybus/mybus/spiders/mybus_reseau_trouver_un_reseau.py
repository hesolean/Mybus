import scrapy


class MybusReseauTrouverUnReseauSpider(scrapy.Spider):
    name = "mybus_reseau_trouver-un-reseau"
    allowed_domains = ["mybus.io"]
    start_urls = ["https://mybus.io/reseaux/trouver-un-reseau"]

    def parse(self, response):
        pass
