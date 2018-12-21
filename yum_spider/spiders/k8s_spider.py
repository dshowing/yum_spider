# -*- coding: utf-8 -*-
import scrapy
import lxml
import sys
import os

class K8sSpider(scrapy.Spider):
    name = 'k8s-spider'
    allowed_domains = ['https://packages.cloud.google.com/yum/repos']
    start_urls = ['https://packages.cloud.google.com/yum/repos/']
    repo_url = 'https://packages.cloud.google.com/yum/repos'
    url_list = []
    k8s_dir = 'D:\PyCharm_Pjt\yum_spider\Repos_k8s\\'

    def parse(self, response):

        a1 = response.xpath("//a[contains(@href,'kube')]/@href")
        a1_list = a1.extract()
        for n, a in zip(range(20), a1_list):
            os.mkdir(self.k8s_dir + a[11:])
            url = self.repo_url + a[11:]
            self.url_list.append(url)

        print(self.url_list)

        for url2 in self.url_list:



    def url_add(self, url):
        second_url = self.allowed_domains + url
        return second_url

