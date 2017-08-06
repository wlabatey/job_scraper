#/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from job_scraper.spiders.stackoverflow import StackOverflowSpider
from job_scraper.spiders.dicer import DiceSpider
from crochet import setup
setup()

runner = CrawlerRunner()
runner.crawl(StackOverflowSpider)
runner.crawl(DiceSpider)
d = runner.join()
