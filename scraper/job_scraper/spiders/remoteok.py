#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Remember we are using python 2 at the moment
from __future__ import print_function

import scrapy
import re
import json
from pprint import pprint

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from job_scraper.items import Job
from datetime import datetime

class RemoteOKSpider(Spider):
    name = "remoteOK"
    allowed_domains = ["remoteok.io"]

    def __init__(self, search_params=None, *args, **kwargs):
        super(RemoteOKSpider, self).__init__(*args, **kwargs)

        if not search_params:
            raise ValueError("No search terms given")

        self.search_terms = search_params.split(",")

    def start_requests(self):
        # Trying to simply parse the remote-jobs json file at the moment,
        # as the site search URLs don't look to be standardized.
        yield scrapy.Request("https://remoteok.io/remote-jobs.json", self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response)
        pprint(jsonresponse)
        items = []
        # for job in jsonresponse[0].items():
            # item = Job()
            # item["title"] = job.position
            # item["company"] = job["company"]
            # item["location"] = "Remote"
            # item["url"] = job["url"]
            # item["date_posted"] = job["date"]
            # item["salary"] = ""
            # item["tags"] = job["tags"]
            # item["crawl_timestamp"] = datetime.now().strftime("%H:%M:%S %Y-%m-%d") 
            # item["job_board"] = "RemoteOK"
            # items.append(item)
        return items
