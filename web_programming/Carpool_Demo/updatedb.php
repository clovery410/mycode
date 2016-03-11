<?php
	session_start();
	// $route_id=$_POST['route_id'];
	$route_id = $_SESSION['SESS_ROUTE_ID'];
	$start = $_SESSION['SESS_DEPART'];
	$end = $_SESSION['SESS_DEST'];
	$eat = $_SESSION['SESS_EAT'];

	$servername = "localhost";
  $username = "root";
  $password = "root";
  $dbname = "myDB";

	$conn = new mysqli($servername, $username, $password, $dbname);
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
		}
	$sql="UPDATE Routes SET Routes.max_people = Routes.max_people - 1 WHERE Routes.route_id = $route_id";
	if ($conn->query($sql)===TRUE){
		$sql1="SELECT Drivers.email FROM Drivers, Routes WHERE Drivers.driver_id = Routes.driver_id AND Routes.route_id = $route_id";
		$result1 = $conn->query($sql1);
		if ($result1->num_rows>0){
			while ($row=$result1->fetch_assoc()){
				$to=$row[email];
			}
		}
		$subject = "New Carpool Request from SCUCARPOOL.com";
		// $message="Dear Driver, there is a new carpool request from North San Jose to SCU!";
		$message = 'Dear Driver, \r\n There is a new carpool request from ' . $start. ' to ' . $end . ' at ' . $eat . '. Wish you a good journey!\r\n\r\n Regards,\r\n SCU Carpool';

	$cmd = "curl -s --user 'api:key-01191b9c019e3210694f926765092e4f' \
https://api.mailgun.net/v3/sandboxb71a068eb169468c8ad44c37d884a3ef.mailgun.org/messages \
-F from='SCU Carpool <mailgun@sandboxb71a068eb169468c8ad44c37d884a3ef.mailgun.org>' \
-F to=".$to." \
-F subject='".$subject."' \
-F text='".$message."'";

		shell_exec($cmd);

	}
	else {
   		echo "Error updating record: " . $conn->error;
	}
	$conn->close();

	header("location:confirm_final.php");
	exit();
?>
