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

  // //sql to create table Users
  // $sql = "CREATE TABLE Users (
  //   id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  //   firstname VARCHAR(30) NOT NULL,
  //   lastname VARCHAR(30) NOT NULL,
  //   phone VARCHAR(12) NOT NULL,
  //   email VARCHAR(50) NOT NULL,
  //   psw VARCHAR(50) NOT NULL,
  //   is_driver INT(6) UNSIGNED NOT NULL,
  //   reg_date TIMESTAMP
  // )";

  // //sql to create table Drivers
  // $sql = "CREATE TABLE Drivers (
  //   driver_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  //   email VARCHAR(50) NOT NULL,
  //   car_brand VARCHAR(30) NOT NULL,
  //   car_model VARCHAR(30) NOT NULL,
  //   car_color VARCHAR(30) NOT NULL,
  //   plate_num VARCHAR(10) NOT NULL,
  //   license_num VARCHAR(10) NOT NULL,
  // )";

  //sql to create table Routes
  $sql = "CREATE TABLE Routes (
    route_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    driver_id INT(6) UNSIGNED NOT NULL,
    user_id INT(6) UNSIGNED NOT NULL,
    region CHAR(1) NOT NULL,
    direction INT(1) UNSIGNED NOT NULL,
    max_people INT(1) UNSIGNED NOT NULL,
    stop_0 DATETIME,
    stop_1 DATETIME,
    stop_2 DATETIME,
    stop_3 DATETIME,
    stop_4 DATETIME,
    stop_5 DATETIME,
    stop_6 DATETIME,
    stop_7 DATETIME,
    stop_8 DATETIME,
    stop_9 DATETIME,
    depart VARCHAR(20) NOT NULL,
    dest VARCHAR(20) NOT NULL
  )";

  // //sql to create table Stops
  // $sql = "CREATE TABLE Stops (
  //   stop_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  //   stop_name VARCHAR(20) NOT NULL,
  //   area INT(1) UNSIGNED
  // )";


  if ($conn->query($sql) == TRUE) {
    echo "Table Users created successfully";
  } else {
    echo "Error creating table: " . $conn->error;
  }

  $conn->close();
?>
