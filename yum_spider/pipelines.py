# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import logging

from yum_spider import settings


logger = logging.getLogger(__name__)

class YumSpiderPipeline(object):
    def process_item(self, item, spider):
        if item["come_from"] == 'k8s':
            #logger.warning("-"*10)
            print(item)
        return item

