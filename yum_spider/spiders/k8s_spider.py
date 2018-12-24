# -*- coding: utf-8 -*-
import scrapy
import os
import logging

from yum_spider.items import YumSpiderItem

logger = logging.getLogger(__name__)

class K8sSpider(scrapy.Spider):
    name = 'k8s-spider'
    allowed_domains = ['google.com']

    start_urls = ['https://packages.cloud.google.com/yum/repos/']
    base_url = 'https://packages.cloud.google.com'
    url_list = []
    dir01_list = []

    def parse(self, response):

        ret1 = response.xpath("//a[contains(@href,'kube')]/@href")
        for url in ret1:
            item = {}
            item["come_from"] = 'k8s'
            item["name"] = url.extract()
            item["urls"] = url.extract()
            logger.warning(item)
            # 减少内存占用，生成器
            yield item
            next_url = self.base_url + item["urls"] + 'repodata'
            yield scrapy.Request(
                next_url,
                callback=self.parse_next(next_url)
            )

    def parse_next(self, response):
        pass


        # a1_list = ret1.extract()
        # for n, a in zip(range(20), a1_list):
        #     #创建目录
        #     os.makedirs(self.k8s_dir + a[11:] + '\\repodata')
        #     url = self.base_url + a[11:] + '\\repodata'
        #     self.url_list.append(url)
        #     self.dir01_list.append(a[11:] + '\\repodata')

        # print(self.url_list)

        #for url2, dir01 in zip(self.url_list, self.dir01_list):


