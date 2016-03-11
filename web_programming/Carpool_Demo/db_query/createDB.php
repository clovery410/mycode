<?php
  $servername = "localhost";
  $username = "root";
  $password = "root";

  // Create connection
  $mysqli = new mysqli($servername, $username, $password);
  // Check connection
  if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
  }

  // Create database
  $sql = "CREATE DATABASE myDB";
  if ($mysqli->query($sql) == TRUE) {
    echo "Database created successfully";
  } else {
    echo "Error creating database: " . $mysqli->error;
  }
  echo 'Connected successfully.';

  $mysqli->close();
?>
