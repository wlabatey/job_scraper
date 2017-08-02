# Simple Job Scraper

Searches Stackoverflow & Dice for jobs and saves the results to DynamoDB.

Run `python3 scrape.py` to scrape job sites, save the results to DynamoDB and open `static_page/index.html` in chrome.

## To Do

- Add more job boards (weworkremotely, remotive, indeed, reed).
- Add 'hide' checkbox to each job element.
- Consider adding tabs to display the different job boards separately when they are done.
- ~~Use DynamoDB for storage instead of s3. Use the [AWS Javascript SDK](https://aws.amazon.com/sdk-for-browser/) & [AWS Python SDK](https://aws.amazon.com/sdk-for-python/). Will need to check for existing jobs in table to avoid duplicates on new scrapes. Check pricing.~~ Done. Approx. $2/month. 
- ~~Implement JSON export pipeline to export each spider's results into separate json files, then fetch and display each json file separately.~~
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- ~~Use css grid to display as boxes (4/5 per row)~~

## Future ideas

Possible to implement as a Django web app and write items using Django Models with the [scrapy-djangoitem extension](https://github.com/scrapy-plugins/scrapy-djangoitem).

Should be able to deploy the Django app to AWS Lambda using [Zappa](https://github.com/Miserlou/Zappa).

User searches for keywords and selects which job sites to include in search, scrapy adjusts pipeline to filter job titles by key words and then writes the results to database.
