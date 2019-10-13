# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/600004/company.html']

    def parse(self, response):
        # // *[ @ id = "ml_001"] / table / tbody / tr[1] / td[1] / a
        res_selector=response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()");
        name=res_selector.extract();
        print(name);
        tc_names=response.xpath("//*[@class=\"tc name\"]/a/text()").extract()
        for tc_name in tc_names:
            print(tc_name)

        tc_tls=response.xpath("//*[@class=\"tl\"]/text()").extract()
        for tc_tl in tc_tls:
            print(tc_tl);


        pass
