<!DOCTYPE html>
<?php
	session_start();
	$is_driver = $_SESSION['SESS_IS_DRIVER'];
?>
<html>
<head>
	<title>confirm_final</title>
	<link rel="stylesheet" type="text/css" href="css/confirm_final.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
	<?php
		if ($is_driver == 0) {
			echo '<meta http-equiv="refresh" content="3;url=home.php">';
		} else {
			echo '<meta http-equiv="refresh" content="3;url=driver_home.php">';
		}
	?>
	<!-- <meta http-equiv="refresh" content="3;url=first_page.html"> -->
</head>
<body>
    <div id = "header">
			<?php
			if ($is_driver == 0) {
				echo '<a href="home.php">
								<h1 id="scu">SCU</h1>
								<h1 id="carpool">Carpool</h1>
						 </a>';
			} else {
				echo '<a href="driver_home.php">
								<h1 id="scu">SCU</h1>
								<h1 id="carpool">Carpool</h1>
							</a>';
			}
			?>
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
		<div id="content">
			<p>Congratulations!
				<br/>Your request has been submmited to the driver!
			</p>
			<p class="tip">
				If your browser doesn't jump automatically, please
			</p>
			<a id="homepage" href="first_page.html">click here</a>
			<p class="tip">
				.
			</p>
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
