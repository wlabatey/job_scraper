const div = document.querySelector('.jobsGrid'); 
const frag = document.createDocumentFragment();
const checkboxes = document.querySelectorAll('input[type=checkbox]');
const dynamodb = new AWS.DynamoDB();
const params = {
  TableName: 'jobScraper',
};

dynamodb.scan(params, function(err, data) {
  if (err) {
    console.log(err, err.stack);
  } else {
    data.Items.forEach(function(el, i) {
      // Loop through items and create elements
      var jobDiv = document.createElement('div');
      jobDiv.className = 'job ' + el.job_board.S;
      var jobTitle =  document.createElement('p');
      var boldTitle =  document.createElement('b');
      var link = document.createElement('a');
      link.innerHTML = el.title.S;
      link.href = el.url.S;
      link.target = '_blank';
      boldTitle.appendChild(link);
      jobTitle.appendChild(boldTitle);
      jobDiv.appendChild(jobTitle);
      jobDiv.appendChild( document.createElement('p') ).innerHTML = el.company.S;
      jobDiv.appendChild( document.createElement('p') ).innerHTML = el.location.S;
      jobDiv.appendChild( document.createElement('p') ).innerHTML = el.date_posted.S;
      jobDiv.appendChild( document.createElement('p') ).innerHTML = el.salary.S;
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
