# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class JobScraperPipeline(object):
    def process_item(self, item, spider):
        
        keywords = ['dev ops', 'devops', 'aws', 'cloud', 'linux']

        excluded_words = ['asp.net', 'java', 'c#', 'web developer']

        title = item['title'].lower()

        if any(keyword in title for keyword in excluded_words):
            raise DropItem("Job title contained excluded word")
        elif any(keyword in title for keyword in keywords):
            return item
        else:
            raise DropItem("Job title doesn't contain our search terms")
