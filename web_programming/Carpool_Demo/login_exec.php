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
  $email = mysqli_real_escape_string($conn, $_POST['email']);
  $password = mysqli_real_escape_string($conn, $_POST['password']);

  // echo "Your email after escaping: {$email}<br>";
  // echo "Your password after escaping: {$password}<br>";

  //Input validations
  if ($email == '') {
    $errmsg_arr[] = 'Username missing';
    $errflag = true;
  }
  if ($password == '') {
    $errmsg_arr[] = 'Password missing';
    $errflag = true;
  }

  //If there are input validations, redirect back to the login form
  if ($errflag) {
    session_write_close();
    header("location: login.php");
    exit();
  }

  //Create query
  $sql = "SELECT * FROM Users WHERE email = '$email' AND psw = '$password'";
  // $result = mysqli_query($conn, $sql);
  $result = $conn->query($sql);
  // echo "Count of users with the same email and password = " . $result->num_rows;

  //Check whether the query was successful or not
  if ($result) {
    if ($result->num_rows == 1) {
      //Login successful
      $row = mysqli_fetch_array($result);
      session_regenerate_id();
      $_SESSION['SESS_USER_ID'] = $row['id'];
      $_SESSION['SESS_FIRST_NAME'] = $row['firstname'];
      $_SESSION['SESS_LAST_NAME'] = $row['lastname'];
      $_SESSION['SESS_EMAIL'] = $row['email'];
      $_SESSION['SESS_IS_DRIVER'] = $row['is_driver'];
      $_SESSION['SESS_PHONE'] = $row['phone'];
      session_write_close();
      if ($_SESSION['SESS_IS_DRIVER'] == 0) {
        header("location: home.php");
        exit();
      } else {
        header("location: driver_home.php");
        exit();
      }
    } else {
      //Login failed
      $errmsg_arr[] = 'email or password not found';
      $errflag = true;
      if ($errflag) {
        $_SESSION['ERRMSG_ARR'] = $errmsg_arr;
        session_write_close();
        header("location: login.php");
        exit();
      }
    }
  } else {
    die ("Query failed");
  }

  $conn->close();
?>
