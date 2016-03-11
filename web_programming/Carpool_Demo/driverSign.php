<?php
  session_start();

  //Include database connection details
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

  //Array to store validation errors
  $errmsg_arr = array();

  //Validation error flag
  $errflag = false;

  // Function to sanitize values received from the form. Prevents SQL injection
  // function clean ($str) {
  //   $str = @trim($str);
  //   if (get_magic_quotes_gpc()) {
  //     $str = stripslashes($str);
  //   }
  //   return mysqli_real_escape_string($str);
  // }

  //Sanitize the POST values
  // $email = clean($_POST['email']);
  // $password = clean($_POST['password']);
  $carBrand = mysqli_real_escape_string($conn, $_POST['carbrand']);
  $carModel = mysqli_real_escape_string($conn, $_POST['carmodel']);
  $carColor = mysqli_real_escape_string($conn, $_POST['carcolor']);
  $carPlate = mysqli_real_escape_string($conn, $_POST['carnum']);
  $license = mysqli_real_escape_string($conn, $_POST['drivingnum']);

  // //Debuging Purpose
  // echo "Your carBrand after escaping: {$carBrand}<br>";
  // echo "Your License after escaping: {$carModel}<br>";
  // echo "Your carBrand after escaping: {$carColor}<br>";
  // echo "Your License after escaping: {$carPlate}<br>";
  // echo "Your License after escaping: {$license}<br>";

  // Input validations
  if ($carBrand == '') {
    $errmsg_arr[] = 'Car Brand Missing';
    $errflag = true;
  }


  if ($carModel == '') {
    $errmsg_arr[] = 'Car Model Missing';
    $errflag = true;
  }


  if($carColor == '') {
    $errmsg_arr[] = 'Color Missing';
    $errflag = true;
  }

  if($carPlate == '') {
    $errmsg_arr[] = 'Plate Number Missing';
    $errflag = true;
  }


  if($license == '') {
    $errmsg_arr[] = 'Lincense Number Missing';
    $errflag = true;
  }

  //If there are input validations, redirect back to the login form
  if ($errflag) {
    session_write_close();
    // echo "Typing error";
    header("location: log2.php");
    exit();
  }


  // Create query
  $email = $_SESSION['SESS_EMAIL'];
  $sql = "INSERT INTO Drivers (email, car_brand, car_model, car_color, plate_num, license_num)
  VALUES ('$email', '$carBrand', '$carModel', '$carColor', '$carPlate', '$license');";

  // $sql = "INSERT INTO Drivers (email, car_brand, car_model, car_color, plate_num, license_num)
  // VALUES ('ytong@gmail.com','subaru','outback','red', '34567654','123345')";

  if ($conn->query($sql) === TRUE) {
    // Insert successful
    $driver_id = $conn->insert_id;
    $update = "UPDATE Users SET is_driver = '$driver_id' WHERE email = '$email'";
    if ($conn->query($update) === TRUE) {
      $_SESSION['SESS_IS_DRIVER'] = $driver_id;
      session_write_close();
      header("location: driver_home.php");
      exit();
    } else {
      // Insert failed
      echo "Error: " . $update . "<br>" . $conn->error;
    }
  } else {
    // Insert failed
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  // for test only
  // $sql = "INSERT INTO Users (firstname, lastname, phone, email, psw)
  // VALUES ('YING', 'TONG', '6503355', '$email', '123456')";
  // if($conn->query($sql) === TRUE) {
  //   echo "insert test case successful";
  // }


  // // Upadate User Table, set is_driver
  // $sql = "UPDATE Users SET is_driver = '$driver_id' WHERE email = '$email'" ;
  // if ($conn->query($sql) === TRUE) {
  //   echo "Record updated successfully";
  //   header("location:home_driver.php");
  // } else {
  //   echo "Error updating record: " . $conn->error;
  // }

  $conn->close();

?>
