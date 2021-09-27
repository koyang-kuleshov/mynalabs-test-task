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
    COUNT = 50

    def parse(self, response):
        '''Summary of parse.

        Args:
            response: default response.
        '''
        key_pharases = ['man face glasses',
                        'woman face glasses', 'лицо в очках']
        for k_phrase in key_pharases:
            yield response.follow(response.url,
                                  callback=self.get_k_pharase_url,
                                  cb_kwargs={'k_phrase': k_phrase},
                                  dont_filter=True)

    def get_k_pharase_url(self, response, k_phrase):
        '''Summary of get_k_pharase_url.

        Args:
            response
            k_phrase |str| Search query
        '''
        for offset in range(0, 500, self.COUNT):
            params  = {
                'q': k_phrase,
                'license': 'public',
                'imageType': 'photo',
                'imageContent': 'face',
                'count': self.COUNT,
                'minWidth': 256,
                'minHeight': 256
            }
            params.update({'offset': offset})
            params = urlencode(params)
            url = f'{self.start_urls[0]}?{params}'
            print('*' * 5, url, '*' * 5)
            yield response.follow(url,
                                  callback=self.process_json,
                                  dont_filter=True
                                  )

    def process_json(self, response):
        '''Summary of process_json.

        Args:
            response |json| response with data.
        '''
        item = ItemLoader(CollectImagesFromBingItem(), response)
        data = json.loads(response.body)
        try:
            data = data['images']
        except KeyError as err:
            print(err)
        except TypeError as err:
            print(err)
        else:
            for img in data['value']:
                item.add_value('image_urls', img['contentUrl'])
                yield item.load_item()
