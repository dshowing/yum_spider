# -*- coding: utf-8 -*-
import scrapy
import lxml
import sys
import os

class K8sSpider(scrapy.Spider):
    name = 'k8s-spider'
    allowed_domains = ['https://packages.cloud.google.com/yum/repos']
    start_urls = ['https://packages.cloud.google.com/yum/repos/']

    def parse(self, response):
        #filename = "k8s_repo.html"
        #with open(filename, 'w') as f:
        #    f.write(response.body.decode('utf-8'))

        a_m_t = response.xpath("//a[contains(@href,'kube')]/@href")
        for a in a_m_t:
            print(a)

    # def get_detail(self, response):
    #
    #     item_loader = ArithmeticError(item=K8sItem(), response=response)
    #
    #     item_loader.add_xpath('title', '//')
        pass
