'''Collect data about images.'''
from time import sleep

import scrapy
from scrapy.loader import ItemLoader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from collect_images_from_bing.items import CollectImagesFromBingItem

class CollectImagesSpider(scrapy.Spider):
    '''CollectImagesSpider main class for collecting image's urls.'''
    name = 'collect-images'
    allowed_domains = ['yandex.ru']
    start_urls = ['https://yandex.ru/images/search?text=%D0%BB%D0%B8%D1%86%D0%BE%20%D0%B2%20%D0%BE%D1%87%D0%BA%D0%B0%D1%85']

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        executable_path='/usr/local/bin/geckodriver',
        firefox_binary='/usr/bin/firefox',
        options=options
    )

    def parse(self, response):
        '''Summary of parse.

        Args:
            response: default response.
        '''
        item = ItemLoader(CollectImagesFromBingItem(), response)
        self.driver.get(self.start_urls[0])
        sleep(5)
        media_col = self.driver.find_element_by_xpath('//body')
        while True:
            for _ in range(15):
                media_col.send_keys(Keys.PAGE_DOWN)
                sleep(1)
            imgs = self.driver.find_elements_by_xpath(
                '//div[contains(@class, "serp-item" )]'
                '/a[contains(@class, "serp-item__link")]'
                '/img[contains(@class, "serp-item__thumb")]'
            )
            for img in imgs:
                item.add_value('image_urls', img.get_attribute('src'))
                yield item.load_item()
            sleep(5)
        self.driver.quit()

