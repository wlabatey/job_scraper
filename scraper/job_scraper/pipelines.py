# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter

class JobScraperPipeline(object):
    def process_item(self, item, spider):
        keywords = ['dev ops', 'devops', 'aws', 'cloud', 'linux']
        excluded_words = ['asp.net', 'java', 'c#', 'web developer', 'c++', 
                'windows', 'qa', 'support', '.net', 'manager', 'sales', 
                'marketing', 'senior', 'snr', 'salesforce', 'crm']
        title = item['title'].lower()
        if any(keyword in title for keyword in excluded_words):
            raise DropItem("Job title contained excluded word")
        elif any(keyword in title for keyword in keywords):
            return item
        else:
            raise DropItem("Job title doesn't contain our search terms")

class DuplicatesPipeline(object):
    def __init__(self):
        self.title_company = set()

    def process_item(self, item, spider):
        job_title_company = item['title'] + item['company']
        if job_title_company in self.title_company:
            raise DropItem("Duplicate item found: %s" % (item))
        else: 
            self.title_company.add(job_title_company)
            return item

class JsonExportPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('./json/%s.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class DynamoDBPipeline(object):
    def __init__(self):
        self.items = [] 

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        print('Spider %s has started.' % spider.name)

    def spider_closed(self, spider):
        print('Spider %s has finished.' % spider.name) 
        print('Writing batch to DynamoDB...') 
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        table = dynamodb.Table('jobScraper')
        with table.batch_writer(overwrite_by_pkeys=['jobId']) as batch:
            for item in self.items:
                batch.put_item(
                    Item=item        
                ) 
        self.items=[]

    def process_item(self, item, spider):
        currentItem={
            'jobId': str(item['title']+item['company']),
            'title': str(item['title']),
            'location': str(item['location']),
            'company': str(item['company']),
            'url': str(item['url']),
            'salary': str(item['salary']),
            'date_posted': str(item['date_posted']),
            'crawl_timestamp': str(item['crawl_timestamp']),
            'job_board': str(item['job_board']),
        }        
        self.items.append(currentItem.copy())
        return item
