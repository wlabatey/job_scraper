#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Remember we are using python 2 at the moment
from __future__ import print_function

import scrapy
import re

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import Job
from datetime import datetime

class StackOverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]

    def __init__(self, search_params=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)

        if not search_params:
            raise ValueError("No search terms given")

        self.search_terms = search_params.split(",")

    def start_requests(self):
        location = "London%2C+United+Kingdom"
        distance = "20&u=Miles"
        search_query = "sort=p&q=%s&l=%s&d=%s" 
        base_url = "https://stackoverflow.com/jobs?"
        start_urls = []

        # No longer need to loop through search terms for now. Assuming 1 search at a time.

        # for i, word in enumerate(self.search_terms):
            # start_urls.append(base_url + search_query % (self.search_terms[i], location, distance))

        start_urls.append(base_url + search_query % (self.search_terms, location, distance))

        return [ scrapy.http.Request(url = start_url) for start_url in start_urls ]

    def parse(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "-job-item")]')
        items = []
        for job in jobs:
            item = Job()
            item["title"] = job.xpath('.//a[@class="job-link"]/text()').extract()[0]
            item["company"] = job.xpath('.//div[@class="-name"]/text()').extract()[0].strip()
            item["location"] = re.sub(r'\W+', '', job.xpath('.//div[@class="-location"]/text()').extract()[0].strip())
            item["url"] = job.xpath('.//a[@class="job-link"]/@href').extract()[0]
            item["date_posted"] = job.xpath('.//p[contains(@class, "-posted-date")]/text()').extract()[0].strip()
            item["salary"] = job.xpath('.//span[@class="-salary"]/text()').extract_first(default='n/a').strip()
            item["tags"] = job.css('.-tags p a.post-tag::text').extract()
            item["crawl_timestamp"] = datetime.now().strftime("%H:%M:%S %Y-%m-%d") 
            item["job_board"] = "stackOverflow"
            items.append(item)
        return items
