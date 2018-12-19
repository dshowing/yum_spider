# -*- coding: utf-8 -*-
import scrapy
import lxml
import sys
import os


class K8sSpiderSpider(scrapy.Spider):
    name = 'k8s-spider'
    allowed_domains = ['https://packages.cloud.google.com/yum/repos']
    start_urls = ['https://packages.cloud.google.com/yum/repos/']

    def parse(self, response):
        #filename = "repo.html"
        #with open(filename, 'w') as f:
        #    f.write(response.body.decode('utf-8'))


        # context = response.xpath('/html/head')
        # title = context.extract_first()
        # print(title)

        a_m_t = response.xpath("//a[contains(@href,'kube')]/@href")
        for a in a_m_t:
            print(a)
        pass
