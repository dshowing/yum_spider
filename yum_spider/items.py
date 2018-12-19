# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

from scrapy.loader.processors import MapCompose, TakeFirst


class YumSpiderItem(ItemLoader):
    # define the fields for your item here like:
    # name = scrapy.Field()
    default_output_processor = TakeFirst()


class K8sItem(scrapy.Item):

    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()


    pass
