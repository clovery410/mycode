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

  $direction = mysqli_real_escape_string($conn, $_POST['direction']);
  $region = mysqli_real_escape_string($conn, $_POST['area']);
  $firststop = mysqli_real_escape_string($conn, $_POST['first_stop']);
  $laststop = mysqli_real_escape_string($conn, $_POST['last_stop']);
  $time = mysqli_real_escape_string($conn, $_POST['time']);
  // $date = mysqli_real_escape_string($conn, $_POST['date']);
  $maxpeople = $_POST['max_people'];
  $stops = $_POST['stops'];
  $email = $_SESSION['SESS_EMAIL'];
  $driver_id = $_SESSION['SESS_IS_DRIVER'];
  $user_id = $_SESSION['SESS_USER_ID'];

  //Add departure and destination to stops
  array_push($stops, $firststop, $laststop);
  if ($direction == 0) {
    sort($stops);
  } else {
    rsort($stops);
  }


  // //Debuging Purpose
  // echo "Your direction after escaping: {$direction}<br>";
  // echo "Your area after escaping: {$region}<br>";
  // echo "Your first stop after escaping: {$firststop}<br>";
  // echo "Your last stop after escaping: {$laststop}<br>";
  // echo "Your stops after escaping: {$stops}<br>";
  // echo "Your time after escaping: {$time}<br>";
  // echo "Your max people after escaping: {$maxpeople}<br>";
  // foreach ($stops as $stop) {
  //   echo $stop. "<br/>";
  // }

  //Input validations
  if ($direction == '') {
    $errmsg_arr[] = 'Direction missing';
    $errflag = true;
  }
  if ($region == '') {
    $errmsg_arr[] = 'Area missing';
    $errflag = true;
  }
  if ($firststop == '') {
    $errmsg_arr[] = 'First Stop missing';
    $errflag = true;
  }
  if ($laststop == '') {
    $errmsg_arr[] = 'Last Stop missing';
    $errflag = true;
  }
  if ($maxpeople == '') {
    $errmsg_arr[] = 'Maximum People missing';
    $errflag = true;
  }
  if ($time == '') {
    $errmsg_arr[] = 'Time Schedule missing';
    $errflag = true;
  }

  //If there are input validations, redirect back to the login form
  if ($errflag) {
    session_write_close();
    header("location: publish_route.php");
    exit();
  }

  //Calculate time for each stop
  // $times = array_fill(0, 10, '');
  // array_push($stops, $firststop, $laststop);
  // if ($direction == 0) {
  //   sort($stops);
  // } else {
  //   rsort($stops);
  // }

  // Debug Purpose
  // foreach ($stops as $stop) {
  //   echo $stop;
  // }

  // Initialize some temporary data
  $combine_date = $date . ' ' . $time;
  $date = date('Y-m-d H:i:s', strtotime($combine_date));
  $base = 10;
  $first = True;

  // Previous
  // foreach ($stops as $stop) {
  //   $diff = ($stop - $pre) * $base;
  //   // $curr = DateTime::createFromFormat('j-M-Y', '15-Feb-2009');
  //   $date->add(new DateInterval('PT' . $diff . 'M'));
  //   $times[$stop] = $date->format('Y-m-d H:i:s');
  //   $pre = $stop;
  //   // $time = $new_time;
  // }
  // //Create query
  // foreach ($times as $tt) {
  //   echo $tt . "<br/>";
  // }
  $get_start = "SELECT stop_name FROM Stops WHERE area = '$region' AND sub_index = '$firststop'";
  $get_end = "SELECT stop_name FROM Stops WHERE sub_index = '$laststop' AND area = '$region'";
  $depart = ($conn->query($get_start))->fetch_assoc()['stop_name'];

  // if ($depart == TRUE) {
  //   echo $depart->fetch_assoc()['stop_name'];
  // } else {
  //   echo "Error: " . $get_start . "<br>" . $conn->error;
  // }

  $dest = ($conn->query($get_end))->fetch_assoc()['stop_name'];
  // if ($dest == TRUE) {
  //   echo $dest->fetch_assoc()['stop_name'];
  // } else {
  //   echo "Error: " . $get_end . "<br>" . $conn->error;
  // }

  $sql = "INSERT INTO Routes (driver_id, user_id, region, direction, max_people, depart, dest)
  VALUES ('$driver_id', '$user_id', '$region', '$direction', '$maxpeople', '$depart', '$dest');";

  if ($conn->query($sql) === TRUE) {
    $last_id = $conn->insert_id;
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  foreach ($stops as $stop) {
    if ($first === False) {
      if ($direction == 1) {
        $diff = ($pre - $stop) * $base;
      } else {
        $diff = ($stop - $pre) * $base;
      }

      $curr_date = strtotime($date);
      $future_date = $curr_date + 60 * $diff;
      $date = date('Y-m-d H:i:s', $future_date);
      $pre = $stop;
    } else {
      $pre = $stop;
      $first = False;
    }
    switch ($stop) {
      case '0':
        $update = "UPDATE Routes SET Routes.stop_0 = '$date' WHERE route_id = $last_id";
        break;
      case '1':
        $update = "UPDATE Routes SET Routes.stop_1 = '$date' WHERE route_id = $last_id";
        break;
      case '2':
        $update = "UPDATE Routes SET Routes.stop_2 = '$date' WHERE route_id = $last_id";
        break;
      case '3':
        $update = "UPDATE Routes SET Routes.stop_3 = '$date' WHERE route_id = $last_id";
        break;
      case '4':
        $update = "UPDATE Routes SET Routes.stop_4 = '$date' WHERE route_id = $last_id";
        break;
      case '5':
        $update = "UPDATE Routes SET Routes.stop_5 = '$date' WHERE route_id = $last_id";
        break;
      case '6':
        $update = "UPDATE Routes SET Routes.stop_6 = '$date' WHERE route_id = $last_id";
        break;
      case '7':
        $update = "UPDATE Routes SET Routes.stop_7 = '$date' WHERE route_id = $last_id";
        break;
      case '8':
        $update = "UPDATE Routes SET Routes.stop_8 = '$date' WHERE route_id = $last_id";
        break;
      case '9':
        $update = "UPDATE Routes SET Routes.stop_9 = '$date' WHERE route_id = $last_id";
        break;
      default:
        echo "NO Match";
    }
    $conn->query($update);
  }

  //$date->add(new DateInterval('PT' . $diff . 'M'));
  header("location: driver_home.php");
  exit();

  // //Check whether the query was successful or not
  // if ($result) {
  //   //Login successful
  //   session_regenerate_id();
  //   $_SESSION['SESS_USER_ID'] = $result->insert_id;
  //   $_SESSION['SESS_FIRST_NAME'] = $firstname;
  //   $_SESSION['SESS_LAST_NAME'] = $lastname;
  //   $_SESSION['SESS_EMAIL'] = $email;
  //   //Not sure if need this
  //   //$_SESSION['SESS_IS_DRIVER'] = null;
  //   session_write_close();
  //   header("location: home.php");
  //   exit();
  // } else {
  //   die ("Query failed");
  // }

  $conn->close();
?>
