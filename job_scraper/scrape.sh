#/bin/bash

scrapy crawl StackOverflow -o so.json -t json
s3cmd put so.json --acl-public s3://jobs-json
