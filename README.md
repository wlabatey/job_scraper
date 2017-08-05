# Simple Job Scraper

Searches Stackoverflow & Dice for jobs and saves the results to DynamoDB.

Run `python3 scrape.py` to scrape job sites, save the results to DynamoDB and open `static_page/index.html` in chrome.

## To Do

- ~~Create a Lambda deployment package of the scrapy project & test (See links at bottom).~~ Done, but gives error after 1st run. See links below.
- Add more job boards (weworkremotely, remotive, indeed, reed).
- ~~Use DynamoDB for storage instead of s3. Use the [AWS Javascript SDK](https://aws.amazon.com/sdk-for-browser/) & [AWS Python SDK](https://aws.amazon.com/sdk-for-python/). Will need to check for existing jobs in table to avoid duplicates on new scrapes. Check pricing.~~ Done. Approx. $2/month. 
- ~~Implement JSON export pipeline to export each spider's results into separate json files, then fetch and display each json file separately.~~
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- ~~Use css grid to display as boxes (4/5 per row)~~

## Future ideas

Should be able to deploy scrapy as a lambda function which is invokable from API gateway, then host static page in S3.

Create a button to get new results which calls the API and invokes the lambda function, writing the new results to DynamoDB and then rebuild the elements on the page.

Eventually, should be able to do custom searches, select which job sites to include and then pass keywords, excluded words, location, etc. to scrapy.

## Resources

[Run Scrapy From A Script](https://doc.scrapy.org/en/latest/topics/practices.html)

[Scrapy Script](https://github.com/jschnurr/scrapyscript)

[Scrapy Throws ReactorNotRestartable on AWS Lambda](https://stackoverflow.com/questions/42388541/scrapy-throws-error-reactornotrestartable-when-runnning-on-aws-lambda)

[Create an AWS Lambda Deployment Package for Python](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Python)

[AWS Lambda Function Handler for Python](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)
