<?php
  $servername = "localhost";
  $username = "root";
  $password = "root";
  $dbname = "myDB";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  //sql to create table Stops
  $sql = "CREATE TABLE Stops (
    stop_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    stop_name VARCHAR(20) NOT NULL,
    area INT(1) UNSIGNED NOT NULL,
    sub_index INT(1) UNSIGNED NOT NULL
  )";


  if ($conn->query($sql) == TRUE) {
    echo "Table Stops created successfully";
  } else {
    echo "Error creating table: " . $conn->error;
  }

  // Insert all data
  $northBayArea = array("San Francisco","Daly City","Millbrae","San Mateo","Redwood City","Palo Alto","Mountain View","Sunnyvale","Santa Clara", "SCU");
  $southBayArea = array("Gilroy","San Martin","Morgan Hill","Coyote","Westfield Oakridge","Los Gatos","Campbell","Fruitfale","Westfield Valley Fair", "SCU");
  $eastBayArea = array("Oakland","Alameda","San Leandro","Hayward","Union City","Fremont","Newark","Milpitas","San Jose", "SCU");

  $index = 0;
  foreach ($northBayArea as $stop) {
    // echo "$stop";
    $sql = "INSERT INTO Stops (stop_name, area, sub_index)
    VALUES ('$stop', '0', '$index')";
    $index += 1;
    if($conn->query($sql) == TRUE) {
      echo "successfully";
    }else {
      echo "Erro :" . $sql . $con->error;
    }
  }

  $index = 0;
  foreach ($southBayArea as $stop) {
    // echo "$stop";
    $sql = "INSERT INTO Stops (stop_name, area, sub_index)
    VALUES ('$stop', '1', '$index')";
    $index += 1;
    if($conn->query($sql) == TRUE) {
      echo "successfully";
    }else {
      echo "Erro :" . $sql . $con->error;
    }
  }

  $index = 0;
  foreach ($eastBayArea as $stop) {
    // echo "$stop";
    $sql = "INSERT INTO Stops (stop_name, area, sub_index)
    VALUES ('$stop', '2', '$index')";
    $index += 1;
    if($conn->query($sql) == TRUE) {
      echo "successfully";
    }else {
      echo "Erro :" . $sql . $con->error;
    }
  }

  $conn->close();
?>
