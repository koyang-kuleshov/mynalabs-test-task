import scrapy

from itemloaders.processors import TakeFirst


class CollectImagesFromBingItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
