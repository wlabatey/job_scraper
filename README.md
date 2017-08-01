# Simple Job Scraper

Searches Stackoverflow & Dice for jobs and exports the results into json files.

At the moment, json file must be hosted for the html page to work correctly with the javascript fetch api.

Run `python3 scrape.py` to scrape job sites, upload file to s3 & open `static_page/index.html` in chrome to view the results.

## To Do

- Add more job boards (weworkremotely, remotive, indeed, reed).
- Add 'hide' checkbox to each job element.
- Consider adding tabs to display the different job boards separately when they are done.
- ~~Implement JSON export pipeline to export each spider's results into separate json files, then fetch and display each json file separately.~~
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- ~~Use css grid to display as boxes (4/5 per row)~~

## Future ideas

Possible to implement as a Django web app and write items using Django Models with the [scrapy-djangoitem extension](https://github.com/scrapy-plugins/scrapy-djangoitem).

Should be able to deploy the Django app to AWS Lambda using [Zappa](https://github.com/Miserlou/Zappa).

User searches for keywords and selects which job sites to include in search, scrapy adjusts pipeline to filter job titles by key words and then writes the results to database.
