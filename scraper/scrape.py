#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import os.path
import subprocess

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# so = os.path.abspath('json/stackoverflow.json')
# dice = os.path.abspath('json/dice.json')
# spiders = {'stackoverflow': so, 'dice': dice}
# s3_bucket = 's3://jobs-json'
# static_page = os.path.abspath('../site/index.html')

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

# print("Uploading to S3...")
# for v in spiders.values():
    # subprocess.Popen(['/usr/bin/s3cmd', 'put', v, '--acl-public', s3_bucket])

# print("Opening browser...")
# subprocess.Popen(['google-chrome', static_page])
