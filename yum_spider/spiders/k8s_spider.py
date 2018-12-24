# -*- coding: utf-8 -*-
import scrapy
import os
import logging

from scrapy.selector import Selector
from yum_spider.items import YumSpiderItem



#logger = logging.getLogger(__name__)

class K8sSpider(scrapy.Spider):
    name = 'k8s-spider'
    allowed_domains = ['google.com']

    start_urls = ['https://packages.cloud.google.com/yum/repos/']
    base_url = 'https://packages.cloud.google.com'

    repo_dir = "D:\PyCharm_Pjt\yum_spider\Repos_k8s"
    url_list = []
    dir01_list = []

    def parse(self, response):
        selector = Selector(response)

        item = YumSpiderItem()

        ret1 = selector.xpath("//a[contains(@href,'kube')]/@href").extract()
        for urls in ret1:

            dir1 = urls[11:]
            next_url = self.base_url + urls + '/repodata'
            next_dir = self.repo_dir + dir1 + '\\repodata'
            # print('dir is :%s', next_dir)
            # print('url is :%s', next_url)
            # os.makedirs(next_dir)

            item["repodirs"] = next_dir
            item["repourls"] = next_url
            request = scrapy.Request(
                next_url,
                meta={'item': item},
                callback=self.parse_next
            )


            # yield request


    def parse_next(self, response):
        selector = Selector(response)

        item = response.meta('item')
        ret2 = selector.xpath("//body/a/text()")
        print(ret2)
        for filename in ret2:
            file_url = self.base_url + item['urls'] + '/repodata' + filename
            item["filenames"] = filename
            item["file_urls"] = file_url
            yield item


