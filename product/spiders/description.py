# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class DescriptionSpider(scrapy.Spider):
    name = 'description'
    allowed_domains = ['m.prodia.co.id']
    start_urls = ['https://m.prodia.co.id/id/ProdukLayanan/PemeriksaanLaboratorium/14']

    def parse(self, response):
        alfabet = response.xpath('.//div[@id="pilih-alfabet"]/div/text()').extract()
        for i, d in enumerate(alfabet):
            number = i + 1
            url = response.xpath('.//div[@id="pilih-alfabet"]/ul[@class="alfabet-item"][{}]/li/a/@href'.format(number)).extract();
            print(url)
            for u in url:
                yield Request(url="https://m.prodia.co.id/" + u, callback=self.parseTitleDesc, meta={'alfabet': d})


    def parseTitleDesc(self, response):
        desc = ""
        if(response.xpath('.//p/text()').extract()[0] == "Belum memiliki akun?"):
            desc = ""  
        else: 
            desc = response.xpath('.//p/text()').extract()[0] 

        yield{
            "Title": response.xpath('.//h2/text()').extract()[0],
            "Alfabet": response.meta["alfabet"],
            "Description": desc,
            "Mamfaat Pemeriksaan": response.xpath('.//p/text()').extract()[1]
        }
