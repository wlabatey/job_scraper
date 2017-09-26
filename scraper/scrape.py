#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import os.path
import subprocess

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

spiders = ['stackoverflow']
process = CrawlerProcess(get_project_settings())

for spider in spiders:
    print("Added spider: " + spider)
    process.crawl(spider)
process.start()
print("Finished scraping...")

jobs = []

with open('./json/jobs.json') as job_file:
    jobs = json.load(job_file)

pprint(jobs)
