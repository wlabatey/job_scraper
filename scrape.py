#/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import subprocess

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

so = os.path.abspath('json/stackoverflow.json')
dice = os.path.abspath('json/dice.json')
spiders = {'stackoverflow': so, 'dice': dice}
s3_bucket = 's3://jobs-json'
static_page = os.path.abspath('static_page/index.html')

process = CrawlerProcess(get_project_settings())

for k in spiders.keys():
    print("Added spider: " + k)
    process.crawl(k)
process.start()
print("Finished scraping...")

print("Uploading to S3...")
for v in spiders.values():
    subprocess.Popen(['/usr/bin/s3cmd', 'put', v, '--acl-public', s3_bucket])

print("Opening browser...")
subprocess.Popen(['google-chrome', static_page])
