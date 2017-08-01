#/bin/bash

FILE=./so.json

if [ -e "$FILE" ]; then
  echo "Found old json file. Deleting and proceeding..."
  rm $FILE
else
  echo "No previous json file found. Proceeding..."
fi

scrapy crawl StackOverflow -t json -o $FILE
s3cmd put so.json --acl-public s3://jobs-json
google-chrome ./static_page/index.html
