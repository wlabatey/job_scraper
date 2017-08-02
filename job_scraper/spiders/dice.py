#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import DiceItem
from datetime import datetime

class DiceSpider(CrawlSpider):
    name = "dice"
    allowed_domains = ['uk.dice.com']
    allowed_urls = ['http://uk.dice.com/index.php', 'uk.dice.com/IT-jobs']
    search_terms = ['dev+ops', 'devops', 'junior+dev+ops', 'junior+devops', 'aws', 'cloud', 'linux']
    location = 'London'
    distance = '5'
    search_query = 'SearchTerms=%s&LocationSearchTerms=%s&Mode=AdvertSearch&lang=en&Radius=%s' 
    base_url = 'http://uk.dice.com/index.php?'
    start_urls = []
    for i, word in enumerate(search_terms):
        start_urls.append(base_url + search_query % (search_terms[i], location, distance))

    rules = (
        Rule(LinkExtractor(allow=(''), restrict_xpaths=('//a[@id="NextPage2"]')), callback="parse_items", follow=True),        
    )

    def parse_items(self, response):
        hxs = Selector(response)
        jobs = hxs.xpath('//div[contains(@class, "searchResultTitle")]')
        items = []
        for job in jobs:
            item = DiceItem()
            item["title"] = job.xpath('.//h2/a[contains(@id, "TITLE")]/text()').extract()[0].strip()
            company = job.xpath('.//p/span[contains(@id, "CONTACT_OFFICE")]/text()').extract()
            item["company"] = company[0].strip() if company else "n/a"
            item["location"] = job.xpath('.//p/span[contains(@id, "FREE_LOCATION")]/text()').extract()[0].strip()
            item["url"] = job.xpath('.//h2/a[contains(@id, "TITLE")]/@href').extract()[0]
            item["date_posted"] = job.xpath('.//p/span[contains(@id, "POSTED_DATE")]/text()').extract()[0].strip()
            salary = job.xpath('.//p/span[contains(@id, "SALARY")]/text()').extract()
            item["salary"] = salary[0].strip() if salary else "n/a"
            item["crawl_timestamp"] = datetime.now().strftime("%H:%M:%S %Y-%m-%d") 
            item["job_board"] = "dice"
            items.append(item)
        return items
