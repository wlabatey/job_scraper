# Simple Job Scraper with scrapy.

Searched Stackoverflow for dev ops jobs and exports the result into a json file.

~~Viewable in jobs.php locally by running docker-compose with the php image.~~

Viewable in `static_page/index.html`. 

## To Do
- ~~Use javascript instead of php to dynamically create the page elements.~~
- ~~Host the static file on S3.~~
- Create a lambda function to run once/twice daily to update the json file, which is also in s3.
- Consider writing to a database (dynamoDB?) instead of using json. Need persistence but also minimal cost.
- Add more job boards
- Add 'hide' checkbox to each job element
- Use css grid to display as boxes (4/5 per row)
- Consider adding tabs to display the different job boards separately when they are done.
