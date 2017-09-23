# Simple Job Scraper

~~Searches Stackoverflow & Dice for jobs and saves the results to DynamoDB.~~

Job site aggregator. Scrapes results from multiple job sites and returns result to web page.

Uses AWS Lambda, Python, Scrapy & Travis CI.

Will eventually use Django for the web app. 

## To Do (Adapt to new architecture)

- Scrapy saves job items as list of dictionaries (1 per job)
- Convert list of dicts to json object
- Return json of processed jobs from AWS Lambda function, build job elements on page from return json.
- Invoke lambda function directly from static page using AWS Javascript SDK. (Remove DynamoDB)
- Add search box and button to front end to invoke lambda function. (Start with job titles)
- Pass arguments into scrapy to use for searching, pass data from lambda invocation in javascript from static page.

Avoid using API gateway and DynamoDB. Invoke the lambda function directly from the page and then return the results. No need to store long term if it's fast enough!

### Resources:

[Scrapydo documentation (See the scrapydo.run_spider example)](https://github.com/rmax/scrapydo)

[Pass user defined arguments into scrapy spiders](https://stackoverflow.com/questions/15611605/how-to-pass-a-user-defined-argument-in-scrapy-spider)

[Save scrape results into list of dicts](https://stackoverflow.com/a/23574703/8300614)

[Convert list of dicts to json in python](https://stackoverflow.com/questions/21525328/python-converting-a-list-of-dictionaries-to-json)

[Invoke a Lambda Function from javascript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/browser-invoke-lambda-function-example.html)

[Building a python AWS Lambda deployment package](https://medium.com/the-python-backend/hassle-free-python-lambda-deployment-tutorial-script-9c65bcf47e26)

-----

#### Old Resources

[Build An API To Expose An AWS Lambda Function](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)

[Run Scrapy From A Script](https://doc.scrapy.org/en/latest/topics/practices.html)

[Scrapy Script](https://github.com/jschnurr/scrapyscript)

[Scrapy Throws ReactorNotRestartable on AWS Lambda](https://stackoverflow.com/questions/42388541/scrapy-throws-error-reactornotrestartable-when-runnning-on-aws-lambda)

[Create an AWS Lambda Deployment Package for Python](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Python)

[AWS Lambda Function Handler for Python](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)
