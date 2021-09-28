# Mynalabs tesk task

## Install dependencies

`pip install -r requirements.txt`

[Установить geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.29.1) ver. 0.29.1 (970ef713fe58 2021-04-08 23:34 +0200)

[Установить Mozilla Firefox 90.0](https://www.mozilla.org/ru/firefox/all/#product-desktop-release)

## Scrapy

Запуск из директории **collect-images**

`python3 main.py`

## Настройки

Файл в директории **collect-images/collect_from_yandex**
`settings.py`

CLOSESPIDER_ITEMCOUNT = 5000 - Количество item для сбора.\
CONCURRENT_REQUESTS = 16 - Количество одновременных запросов.\
DOWNLOAD_DELAY = 3 - Задержка перед каждым запросом.\
CONCURRENT_REQUESTS_PER_DOMAIN = 4 - Количество запросов на домен.\
AUTOTHROTTLE_START_DELAY = 3 - Начальная задержка для Autothrottle.\
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0 - Среднее количество запросов отправляемое Scrapy.

По умолчанию парсер настроен на неспешный парсинг, чтобы не попасть в бан от Яндекса.

Изображения фильтруются по размеру перед сохранением.

Собранные файлы складываются в папку **process-image/img**

[Собранные файлы](https://disk.yandex.ru/d/8ym8lewALvV5EQ)

[Архив](https://disk.yandex.ru/d/bghj103g4E8AAA)

## Pytorch

Файл в директории **process-images**

`python3 crop-images.py`

Обработанные файлы складываются в папку **processed-imgs**
