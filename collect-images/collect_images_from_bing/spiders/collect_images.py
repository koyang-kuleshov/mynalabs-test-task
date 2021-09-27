'''Collect data about images.'''
import json
from urllib.parse import urlencode

import scrapy
from scrapy.loader import ItemLoader

from collect_images_from_bing.items import CollectImagesFromBingItem

class CollectImagesSpider(scrapy.Spider):
    '''CollectImagesSpider main class for collecting image's urls.'''
    name = 'collect-images'
    allowed_domains = ['microsoft.com']
    start_urls = ['https://api.bing.microsoft.com/v7.0/search']


    def parse(self, response):
        '''Summary of parse.

        Args:
            response: default response.
        '''
        key_pharases = ['"men face glasses"',
                        '"women face glasses"']
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
        '''Summary of process_json.

        Args:
            response |json| response with data.
        '''
        item = ItemLoader(CollectImagesFromBingItem(), response)
        data = json.loads(response.body)
        imgs = data['images']['value']
        for img in imgs:
            item.add_value('image_urls', img['thumbnailUrl'])
            yield item.load_item()
