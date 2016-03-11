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

  $sql = "SELECT Users.firstname, Users.lastname, Users.phone, Drivers.email, Drivers.car_brand, Drivers.car_model, Drivers.car_color, Drivers.plate_num, Drivers.max_people FROM Users, Drivers, Routes WHERE Users.email = Drivers.email AND Drivers.driver_id = Routes.driver_id AND Routes.region = 'A' AND Routes.direction = 0 AND Routes.max_people > 1";
  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
    //output data of each row
    while ($row = $result->fetch_assoc()) {
      echo "driver email: " . $row["email"] . " - Name: " . $row["firstname"] . " " . $row["lastname"] . "<br>";
    }
  } else {
    echo "0 results";
  }

  $conn->close();
?>
