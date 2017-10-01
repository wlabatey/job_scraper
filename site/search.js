const div = document.querySelector('.jobsGrid'); 
const frag = document.createDocumentFragment();
const checkboxes = document.querySelectorAll('input[type=checkbox]');
const searchBox = document.getElementById('searchQuery');
const searchButton = document.getElementById('searchButton');
const lambda = new AWS.Lambda({region: "eu-west-2", apiVersion: '2015-03-31'});
let lambdaParams = {
  FunctionName: 'scraper-test',
  InvocationType: 'RequestResponse',
  LogType: 'None',
};
let lambdaResults;

searchButton.addEventListener("click", function(event) {
  let search_params = searchBox.value;
  console.log(search_params);
  let paramObject = {
    'search_params': search_params,
    'spider': 'stack_overflow'
  };
  lambdaParams.Payload = JSON.stringify(paramObject);
  console.log(lambdaParams);
  div.innerHTML = "";
  searchBox.value = "";

  lambda.invoke(lambdaParams, function(err, data) {
    if (err) {
      console.log(err, err.stack);
    } else {
      lambdaResults = JSON.parse(data.Payload);
      console.log(lambdaResults);
      console.log(data);

      lambdaResults.forEach(function(el, i) {
        // Loop through items and create elements
        var jobDiv = document.createElement('div');
        jobDiv.className = 'job ' + el.job_board;
        var jobTitle =  document.createElement('p');
        var boldTitle =  document.createElement('b');
        var link = document.createElement('a');
        link.innerHTML = el.title;
        link.href = el.url;
        link.target = '_blank';
        boldTitle.appendChild(link);
        jobTitle.appendChild(boldTitle);
        jobDiv.appendChild(jobTitle);
        jobDiv.appendChild( document.createElement('p') ).innerHTML = el.company;
        jobDiv.appendChild( document.createElement('p') ).innerHTML = el.location;
        jobDiv.appendChild( document.createElement('p') ).innerHTML = el.date_posted;
        jobDiv.appendChild( document.createElement('p') ).innerHTML = el.salary;
        el.tags.forEach(function(el, i) {
          jobDiv.appendChild( document.createElement('p') ).innerHTML = el;
        }
        frag.appendChild(jobDiv);
        div.appendChild(frag);
      });

      // After jobs created, then loop through checkboxes and hide if checkbox not checked.
      checkboxes.forEach(function(el, i) {
        var name = '.'+el.name;
        var jobs = document.querySelectorAll(name);
        if (el.checked === false) {
          jobs.forEach(function(el, i) {
            el.style.display = 'none';
          });  
        }

        // Loop through checkboxes and add eventlistener to detect changes and hide/show divs.
        el.addEventListener('change', function(event) {
          jobs.forEach(function(el,i) {
            el.style.display === 'none' ? 
            el.style.display = 'inline-block' :
            el.style.display = 'none';
          });
        });
      });
    }
  });
});
