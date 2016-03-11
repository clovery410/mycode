<!DOCTYPE html>
<?php
  //Start session
  session_start();
 ?>
<html>
<head>
	<title>Become a Driver</title>
	<link href="css/log2.css" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
</head>
<body>
    <div id = "header">
        <div>
        <a href="home.php">
        	<h1 id="scu">SCU</h1>
        	<h1 id="carpool">Carpool</h1>
        </a>
        </div>
		<a href="message_page.php">
			<img id="msg" src="images/message.jpg.png" alt="msg" />
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

    <a id="driver" href="log2.php">Become a Driver
    </a>
    <a id="driver" href="logout.php">Log Out
    </a>
	</div>

	<div id="main">
	<div id="signup">
		<div id="form">
			<form name="driver_signup" action="driverSign.php" method="post">
				<div class="label">Car Brand</div>
				<input type="text" name="carbrand" value=""><br>
				<div class="label">Car Model</div>
				<input type="text" name="carmodel" value=""><br>
				<div class="label">Car Color</div>
				<input type="text" name="carcolor" value=""><br>
				<div class="label">Plate Number</div>
				<input type="text" name="carnum" value=""><br>
				<div class="label">License Number</div>
				<input type="text" name="drivingnum" value=""><br>
				<div id="b">
					<input id="button" type="submit" value="Become a Driver">
				</div>
			</form>
		</div>
	</div>

	<div id="right">
		<p id="head">Register as A Driver</p>
		<img id="img" src="images/driver.jpg" alt="driver" />
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
