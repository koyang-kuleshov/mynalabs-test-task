import json
from urllib.parse import urlencode

import scrapy
from scrapy.loader import ItemLoader

from collect_images_from_bing.items import CollectImagesFromBingItem

class CollectImagesSpider(scrapy.Spider):
    name = 'collect-images'
    allowed_domains = ['microsoft.com']
    start_urls = ['https://api.bing.microsoft.com/v7.0/search']


    def parse(self, response):
        key_pharases = ['"men face +with glasses"',
                        '"women face +with glasses"']
        for k_phrase in key_pharases:
            params  = urlencode({
                'q': k_phrase,
                'license': 'public',
                'imageType': 'photo',
                'imageContent': 'face',
                'minWidth': 256,
                'minHeight': 256
            })
            url = f'{self.start_urls[0]}?{params}'
            yield response.follow(url,
                                  callback=self.process_json)

    def process_json(self, response):
        item = ItemLoader(CollectImagesFromBingItem(), response)
        data = json.loads(response.body)
        imgs = data['images']['value']
        for img in imgs:
            item.add_value('img_url', img['thumbnailUrl'])
            item.add_value('img_width', img['thumbnail']['width'])
            item.add_value('img_height', img['thumbnail']['height'])
            item.add_value('img_format', img['encodingFormat'])
            yield item.load_item()

