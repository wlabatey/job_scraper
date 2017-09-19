# Simple Job Scraper

Searches Stackoverflow & Dice for jobs and saves the results to DynamoDB.

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

-----

## To Do (Old)

- Add button to static page to run Lambda function via api gateway, then clear screen and rebuild elements from DynamoDB when function has finished running.
- Add more job boards (weworkremotely, remotive, indeed, reed).

- Store results as single DynamoDb item in JSON format, identified by hash of user ip + browser identifier, which is attempted to be retrieved on page load. This will allow results stored on a per user basis as a single table item. Add controls to clear results and search again based on new parameters. 

- ~~Create a Lambda deployment package of the scrapy project & test (See links at bottom).~~ Done. Now working in AWS Lambda with scrapydo. 
- ~~Use DynamoDB for storage instead of s3. Use the [AWS Javascript SDK](https://aws.amazon.com/sdk-for-browser/) & [AWS Python SDK](https://aws.amazon.com/sdk-for-python/). Will need to check for existing jobs in table to avoid duplicates on new scrapes. Check pricing.~~ Done. Approx. $2/month. 
- ~~Implement JSON export pipeline to export each spider's results into separate json files, then fetch and display each json file separately.~~
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- ~~Use css grid to display as boxes (4/5 per row)~~

## Future ideas

~~Should be able to deploy scrapy as a lambda function which is invokable from API gateway, then host static page in S3.~~

Create a button to get new results which calls the API and invokes the lambda function, writing the new results to DynamoDB and then rebuild the elements on the page.

Eventually, should be able to do custom searches, select which job sites to include and then pass keywords, excluded words, location, etc. to scrapy.

Should be able to configure how many pages of results to scrape, to be able to speed up scrape process.



## Resources

[Build An API To Expose An AWS Lambda Function](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)

[Run Scrapy From A Script](https://doc.scrapy.org/en/latest/topics/practices.html)

[Scrapy Script](https://github.com/jschnurr/scrapyscript)

[Scrapy Throws ReactorNotRestartable on AWS Lambda](https://stackoverflow.com/questions/42388541/scrapy-throws-error-reactornotrestartable-when-runnning-on-aws-lambda)

[Create an AWS Lambda Deployment Package for Python](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Python)

[AWS Lambda Function Handler for Python](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)
