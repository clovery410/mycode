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

  $sql = "UPDATE Users SET firstname='Xiaoying' WHERE id=3";

  if ($conn->query($sql) == TRUE) {
    echo "Record updated successfully";
  } else {
    echo "Error updating record: " . $conn->error;
  }

  $conn->close();
?>
