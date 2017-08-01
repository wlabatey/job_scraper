#!/usr/bin/env python3

import scrapy
import re
from scrapy import log
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import StackOverflowItem
from datetime import datetime

class StackOverflowSpider(BaseSpider):
    name = "StackOverflow"
    
    # Eventually, we want to loop through this array and perform a new crawl with the search term in the query
    search_terms = ["dev+ops", "devops", "junior+dev+ops", "junior+devops", "aws", "cloud", "linux"]
    location = "London%2C+United+Kingdom"
    distance = "20&u=Miles"
    search_query = 'sort=i&q=%s&l=%s&d=%s' % (search_terms[0], location, distance)
    full_url = 'https://stackoverflow.com/jobs?%s' % (search_query)
    allowed_domains = ['stackoverflow.com']
    start_urls = [full_url]

    def parse(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "-job-item")]')
        self.log(jobs)
        items = []
        for job in jobs:
            item = StackOverflowItem()
            item["title"] = job.xpath('.//a[@class="job-link"]/text()').extract()[0]
            item["company"] = job.xpath('.//div[@class="-name"]/text()').extract()[0].strip()
            item["location"] = re.sub(r'\W+', '', job.xpath('.//div[@class="-location"]/text()').extract()[0].strip())
            item["url"] = job.xpath('.//a[@class="job-link"]/@href').extract()[0]
            item["date_posted"] = job.xpath('.//p[contains(@class, "-posted-date")]/text()').extract()[0].strip()
            item["salary"] = job.xpath('.//span[@class="-salary"]/text()').extract_first(default='n/a').strip()
            item["crawl_timestamp"] = datetime.now().strftime("%H:%M:%S %Y-%m-%d") 
            item["jobBoard"] = "stackOverflow"
            items.append(item)
            self.log(item)
        self.log(items)
        return items
