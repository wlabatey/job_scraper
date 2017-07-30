# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class StackOverflowItem(Item):
    # First page information
    title = Field()
    company = Field()
    location = Field()
    salary = Field()
    date_posted = Field()
    tags = Field()

    # Job advert page information
    job_type = Field()
    experience_level = Field()
    role = Field()

    description = Field()
    requirements = Field()

    # Other
    source_url = Field()
    crawl_timestmap = Field()
    pass
