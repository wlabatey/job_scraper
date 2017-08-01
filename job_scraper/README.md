# Simple Job Scraper with scrapy.

Searches Stackoverflow for dev ops jobs and exports the result into a json file.

At the moment, json file must be hosted for the html page to work correctly with the javascript fetch api.

Viewable in `static_page/index.html`. 

## To Do
- Add more job boards
- Add 'hide' checkbox to each job element
- Consider adding tabs to display the different job boards separately when they are done.
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- ~~Use css grid to display as boxes (4/5 per row)~~

## Future ideas

Consider developing into a php page reading jobs from mysql database, written to by scrapy.

User searches for keywords and selects which job sites to include in search, scrapy adjusts pipeline to filter job titles by key words and then writes the results to database.
