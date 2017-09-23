#/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import scrapydo
import logging
from job_scraper.spiders.stackoverflow import StackOverflowSpider
from job_scraper.spiders.dice import DiceSpider

os.environ['SCRAPY_SETTINGS_MODULE'] = 'job_scraper.settings'
logging.root.setLevel(logging.INFO)
scrapydo.setup()

def start_scrape(event, content):
    scrapydo.run_spider(StackOverflowSpider)
    scrapydo.run_spider(DiceSpider)
