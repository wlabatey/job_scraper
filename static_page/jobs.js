const div = document.querySelector(".jobsGrid"); 
const frag = document.createDocumentFragment();
var checkboxes = document.querySelectorAll('input[type=checkbox]');
let so = 'https://s3.eu-west-2.amazonaws.com/jobs-json/stackoverflow.json';
let dice = 'https://s3.eu-west-2.amazonaws.com/jobs-json/dice.json';
let files = [so, dice];
let jsonData = [];

files.forEach((file,i) => {
  fetch(file)
    .then((res) => res.json())
    .then((json) => jsonData[i] = json)
    .then(() => {
      if (i === 1) {
        // Loop through json and create elements
        jsonData.forEach(function(el, i) {
          el.forEach(function(el,i) {
            var jobDiv = document.createElement('div');
            jobDiv.className = 'job ' + el.jobBoard;
            var jobTitle =  document.createElement('p');
            var boldTitle =  document.createElement('b');
            var link = document.createElement('a');
            link.innerHTML = el.title;
            link.href = el.url;
            link.target = "_blank";
            boldTitle.appendChild(link);
            jobTitle.appendChild(boldTitle);
            jobDiv.appendChild(jobTitle);
            jobDiv.appendChild( document.createElement('p') ).innerHTML = el.company;
            jobDiv.appendChild( document.createElement('p') ).innerHTML = el.location;
            jobDiv.appendChild( document.createElement('p') ).innerHTML = el.date_posted;
            jobDiv.appendChild( document.createElement('p') ).innerHTML = el.salary;
            frag.appendChild(jobDiv);
            div.appendChild(frag);
          });
        });
        
        // After jobs created, then loop through checkboxes and hide if checkbox not checked.
        checkboxes.forEach(function(el, i) {
          var name = '.'+el.name;
          var jobs = document.querySelectorAll(name);
          if (el.checked === false) {
            jobs.forEach(function(el, i) {
              el.style.display = "none";
            });  
          }

          // Loop through checkboxes and add eventlistener to detect changes and hide/show divs.
          el.addEventListener('change', function(event) {
            jobs.forEach(function(el,i) {
              el.style.display === "none" ? 
                el.style.display = "inline-block" :
                el.style.display = "none";
            });
          });
        });
      }
    })
  .catch(err => console.log(err));
});
