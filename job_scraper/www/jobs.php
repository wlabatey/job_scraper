<html>
  <head>
    <title>Dev Ops Job Listings</title>

  <style>
    .job p {
      margin: 0;
    }

    .job {
      display: block;
      margin: 10px 0;
      padding: 5px;
      text-align: center;
      border: solid 1px black;
    }
 </style>  

  </head>

  <body>
    <?php
      $string = file_get_contents("test.json");
      $json_a = json_decode($string, true);
      foreach ($json_a as $mydata) { 
    ?>

    <div class="job">
      <?php 
          echo '<p><a href=' . $mydata['url'] . ' target="_blank"><b>' . $mydata['title'] . '</b></a></p>'; 
          echo '<p>' . $mydata['company'] . '</p>'; 
          echo '<p>' . $mydata['location'] . '</p>'; 
          echo '<p>' . $mydata['date_posted'] . '</p>'; 
          echo '<p>' . $mydata['salary'] . '</p>'; 
      ?>
    </div>

    <?php } ?>

  </body>
</html>
