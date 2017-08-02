#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import StackOverflowItem
from datetime import datetime

class StackOverflowSpider(Spider):
    name = "stackoverflow"
    allowed_domains = ['stackoverflow.com']

    def start_requests(self):
        search_terms = ["dev+ops", "devops", "junior+dev+ops", "junior+devops", "aws", "cloud", "linux"]
        location = "London%2C+United+Kingdom"
        distance = "20&u=Miles"
        search_query = 'sort=i&q=%s&l=%s&d=%s' 
        base_url = 'https://stackoverflow.com/jobs?'
        start_urls = []
        for i, word in enumerate(search_terms):
            start_urls.append(base_url + search_query % (search_terms[i], location, distance))
        return [ scrapy.http.Request(url = start_url) for start_url in start_urls ]

    def parse(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "-job-item")]')
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
            item["job_board"] = "stackOverflow"
            items.append(item)
        return items
