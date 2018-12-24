# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import logging
import os
import urllib.request

from scrapy.pipelines.files import FilesPipeline
from yum_spider.settings import USER_AGENT_LIST
from yum_spider.items import YumSpiderItem
from os.path import basename, dirname, join


class YumSpiderFileDownloadPipeline(FilesPipeline):

    def process_item(self, item, spider):
        return item['file_urls']
        # for header in USER_AGENT_LIST:
        #     req = urllib.request.Request(url=item['fileurls'], header=header)
        #     res = urllib.request.urlopen(req)
        #     file_name = item['filenames']
        #     with open(file_name, 'wb') as f:
        #         f.write(res.read())




