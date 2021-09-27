'''Main.py for scrapping images from Bing API'''
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Settings

from collect_images_from_bing import settings
from collect_images_from_bing.spiders.collect_images import CollectImagesSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proc = CrawlerProcess(settings=crawler_settings)
    crawler_proc.crawl(CollectImagesSpider)
    crawler_proc.start()
