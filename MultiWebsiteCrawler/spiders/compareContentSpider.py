import scrapy
import re
from readability import Document
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "compare_contents"

    start_urls = [
        'https://www.techradar.com/news/samsung-galaxy-watch-active-4-renders-give-us-our-first-look-at-the-likely-design',
    ]

    def parse(self, response):
        blog = '{} {}'.format(Document(response.text).title(), self.cleanhtml(Document(response.text).summary()))
        yield blog

    def cleanhtml(self, raw_html):
      cleanr = re.compile('<.*?>')
      cleantext = re.sub(cleanr, '', raw_html)
      return cleantext
