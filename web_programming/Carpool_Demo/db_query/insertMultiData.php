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

  $sql = "INSERT INTO Users (firstname, lastname, phone, email, psw, is_driver)
  VALUES ('Qianhui', 'Jiang', '6506666666', 'qjiang@scu.edu', '123456', '0');";
  $sql .= "INSERT INTO Users (firstname, lastname, phone, email, psw, is_driver)
  VALUES ('Ying', 'Tong', '6507777777', 'ytong@scu.edu', '654321', '0');";
  $sql .= "INSERT INTO Users (firstname, lastname, phone, email, psw, is_driver)
  VALUES ('Yining', 'Zhang', '6508888888', 'yzhang@scu.edu', '123', '0');";
  $sql .= "INSERT INTO Users (firstname, lastname, phone, email, psw, is_driver)
  VALUES ('Qian', 'Huang', '6509999999', 'qhuang@scu.edu', '456', '0')";

  if ($conn->multi_query($sql) === TRUE) {
      echo "New records created successfully";
  } else {
      echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
?>
