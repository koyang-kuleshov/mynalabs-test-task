import scrapy

from itemloaders.processors import TakeFirst


class CollectImagesFromBingItem(scrapy.Item):
    img_url = scrapy.Field(output_processor=TakeFirst())
    img_filename = scrapy.Field()
    img_width = scrapy.Field(output_processor=TakeFirst())
    img_height = scrapy.Field(output_processor=TakeFirst())
    img_format = scrapy.Field(output_processor=TakeFirst())
