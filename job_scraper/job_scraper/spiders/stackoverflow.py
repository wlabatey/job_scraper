#!/usr/bin/env python3

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import StackOverflowItem

class StackOverflowSpider(CrawlSpider):
    name = "StackOverflow"
    
    # Eventually, we want to loop through this array and perform a new crawl with the search term in the query
    search_terms = ["dev+ops", "devops", "junior+dev+ops", "junior+devops", "aws", "cloud", "linux"]
    location = "London%2C+United+Kingdom"
    distance = "20&u=Miles"
    search_query = 'sort=i&q=%s&l=%s&d=%s' % (search_terms[0], location, distance)
    full_url = 'https://stackoverflow.com/jobs?%s' % (search_query)
    start_urls = [full_url]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="job-link"]')), callback='parse_item', follow=True),
    )

    # def parse_job_page(self, response):
        # function to invoke when fetching job description & requirements from job page


    def parse_item(self, response):
        self.log('\n Crawling %s\n' % (response.url))
        hxs = HtmlXPathSelector(response)
        job = hxs.xpath('//div[@id="job-detail"]')

        keywords = ['dev ops', 'devops', 'aws', 'cloud', 'linux']

        item = StackOverflowItem()
        item["title"] = job.xpath('//a[@class="title job-link"]/text()').extract()
        # item["company"] = job.xpath('//div[@class="-name"]/text()').extract()

        # etc...
        return(item)

