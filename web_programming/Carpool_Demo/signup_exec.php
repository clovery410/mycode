<?php
  session_start();

  //Include database connection details
  // require_once('connection.php');
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

  //Function to sanitize values received from the form. Prevents SQL injection
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
  $firstname = mysqli_real_escape_string($conn, $_POST['firstname']);
  $lastname = mysqli_real_escape_string($conn, $_POST['lastname']);
  $phone = mysqli_real_escape_string($conn, $_POST['phone']);
  $email = mysqli_real_escape_string($conn, $_POST['email']);
  $password = mysqli_real_escape_string($conn, $_POST['newpass']);
  $confirm_password = mysqli_real_escape_string($conn, $_POST['confirmpass']);

  // echo "Your email after escaping: {$email}<br>";
  // echo "Your password after escaping: {$password}<br>";

  //Input validations
  if ($firstname == '') {
    $errmsg_arr[] = 'First Name missing';
    $errflag = true;
  }
  if ($lastname == '') {
    $errmsg_arr[] = 'Last Name missing';
    $errflag = true;
  }
  if ($phone == '') {
    $errmsg_arr[] = 'Phone Number missing';
    $errflag = true;
  }
  if ($email == '') {
    $errmsg_arr[] = 'Email Address missing';
    $errflag = true;
  }
  if ($password == '') {
    $errmsg_arr[] = 'Password missing';
    $errflag = true;
  }
  if ($password != $confirm_password) {
    $errmsg_arr[] = 'Password does not match';
    $errflag = true;
  }

  //If there are input validations, redirect back to the login form
  if ($errflag) {
    session_write_close();
    header("location: login.php");
    exit();
  }

  //Create query
  $sql = "INSERT INTO Users (firstname, lastname, phone, email, psw, is_driver)
  VALUES ('$firstname', '$lastname', '$phone', '$email', '$password', '0');";
  // $result = mysqli_query($conn, $sql);
  $result = $conn->query($sql);
  // echo "Count of users with the same email and password = " . $result->num_rows;

  //Check whether the query was successful or not
  if ($result) {
    //Login successful
    session_regenerate_id();
    $_SESSION['SESS_USER_ID'] = $result->insert_id;
    $_SESSION['SESS_FIRST_NAME'] = $firstname;
    $_SESSION['SESS_LAST_NAME'] = $lastname;
    $_SESSION['SESS_EMAIL'] = $email;
    $_SESSION['SESS_PHONE'] = $phone;
    //Not sure if need this
    //$_SESSION['SESS_IS_DRIVER'] = null;
    session_write_close();
    header("location: home.php");
    exit();
  } else {
    die ("Query failed");
  }

  $conn->close();
?>
