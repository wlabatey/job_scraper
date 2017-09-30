#/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import scrapydo
import logging
import json
from pprint import pprint
from job_scraper.spiders.stackoverflow import StackOverflowSpider
# from job_scraper.spiders.dice import DiceSpider

os.environ["SCRAPY_SETTINGS_MODULE"] = "job_scraper.settings"
logging.root.setLevel(logging.INFO)
scrapydo.setup()

def start_scrape(event, context):
    jobs = []

    spider_args = { 'search_params' : 'dev+ops, devops, junior+dev+ops, junior+devops, aws, cloud, linux' }

    scrapydo.run_spider(StackOverflowSpider, **spider_args)

    print("Finished scraping...")
    with open("/tmp/jobs.json") as job_file:
        jobs = json.load(job_file)

    pprint(jobs)
