<!DOCTYPE html>
<?php
  session_start();
  $is_driver = $_SESSION['SESS_IS_DRIVER'];
?>
<html>
<head>
	<title>Confirmation</title>
	<link href="css/confirmation.css" rel="stylesheet" type="text/css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
</head>
<body>
    <div id = "header">
			<?php
			if ($is_driver == 0) {
				echo '<a href="home.php">';
			} else {
				echo '<a href="driver_home.php">';
			}
			?>
        <h1 id="scu">SCU</h1>
        <h1 id="carpool">Carpool</h1>
        </a>
			<img id="pic" src="images/avatar.jpg" alt="pic"  />
			<span>
				<div id = "slideProfile">
					<div>
						<img class="headShot_profile" src="images/pic.jpg" alt = "HeadShot"/>
						<span>YING TONG</span>
						<p>tongyingkk@gmail.com</p>
						<img id = "star" src = "images/star.png" alt="Rate Star"/>
						<p>Mobile Phone : 650123456</p>
						<p>500 El Camino, Santa Clara,CA</p>
					</div>
				</div>
			</span>
		<a href="message_page.php">
			<img id="msg" src="images/message.jpg.png" alt="msg" />
		</a>
		<?php
			if ($is_driver == 0) {
				echo '<a id="driver" href="log2.php">Become a Driver
							</a>';
			} else {
				echo '<a id="driver" href="publish_route.php">Publish a Route
							</a>';
			}
		?>
		<a id="driver" href="logout.php">Log Out
		</a>
	</div>

		<div id="main">
		<div id="person">
			<img id="p" src="images/pic.jpg" alt="image" />
			<div id="name"><span>

				<!-- Get DB Connection and get Driver Name -->
				<?php
					session_start();
  	 			$route_id = $_POST['route_id'];
					$eat = $_POST['eat'];

					session_regenerate_id();
					$_SESSION['SESS_ROUTE_ID'] = $route_id;
					$_SESSION['SESS_EAT'] = $eat;
					session_write_close();

					$start = $_SESSION['SESS_DEPART'];
					$end = $_SESSION['SESS_DEST'];


					$servername = "localhost";
					$username = "root";
					$password = "root";
					$dbname = "myDB";

					$conn = new mysqli($servername, $username, $password, $dbname);
					if ($conn->connect_error) {
					die("Connection failed: " . $conn->connect_error);
					}

					$fname = "SELECT Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id=Users.id AND Routes.route_id = $route_id";
					// $lname="SELECT Users.lastname FROM Routes,Users WHERE Routes.driver_id=Users.id AND Routes.route_id=$route_id";
					$result = $conn->query($fname);
					if ($result == TRUE) {
						$row = $result->fetch_assoc();
						echo $row[firstname] . ' ' . $row[lastname];
					}
				?>
			</span></div>
		</div>

		<div id="car">
			<table>

				<!-- Get Driver Detail infomation -->
				<?php
					$sql = "SELECT car_brand, car_model, car_color, plate_num FROM Drivers,Routes WHERE Drivers.driver_id = Routes.driver_id AND Routes.route_id = $route_id";
					$result = $conn->query($sql);
					if ($result == TRUE) {
						$row = $result->fetch_assoc();
					} else {
						echo "Error: " . $result . "<br>" . $conn->error;
					}
				?>
				<tr class="row1">
					<td class="col1">
						<?php
							echo $row[car_brand] . "<br>";
						?>
					</td>
					<td class="col1">
						<?php
							echo $row[car_model] . "<br>";
						?>
					</td>
					<td class="col1">
						<?php
							echo $row[car_color] . "<br>";
						?>
					</td>
					<td class="col1">
						<?php
							echo $row[plate_num] . "<br>";
						?>
					</td>
				</tr>
			</table>
		</div>

		<div id="stop">
			<table>
				<tr class="row2">
					<td class="col2">
						<?php
							echo $start;
						?>
					</td>
					<td class="col2">
						<?php
							echo $end;
						?>

					</td>
				</tr>
			</table>
		</div>

		<div id="time">
			<table>
				<tr class="row3">
					<td class="col3">
						<?php
							echo $eat;
						 ?>
					</td>
				</tr>
			</table>
		</div>

		<div id="b">
			<form action="updatedb.php" method="post">
					<input id="button" type="submit" value="Submit">
			</form>
		</div>
	</div>

	<div id="footer">
		<p id="foot">Copyright@Group2 - Web Programming</p>
	</div>

	<script>
			// Profile animation
			$(document).ready(function(){
				$("#pic").click(function(){
					// $("#slideProfile").slideToggle("slow")
					$("#slideProfile").slideDown("slow").css("z-index","1");
				});
				$("#pic").mouseout(function(){
					$("#slideProfile").slideUp("slow");
				});
			});
	</script>
</body>

</html>
