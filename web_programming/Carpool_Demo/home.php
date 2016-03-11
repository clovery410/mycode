<!DOCTYPE html>
<!-- saved from url=(0053)file:///Users/zini/Dropbox/SCU/web_proj/web_proj.html -->
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
	<title>First_Page</title>
	<link type="text/css" rel="stylesheet" href="css/first_page.css">
	<script type="text/javascript" src="js/cf.js"></script>
	<script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.12.0.min.js"></script>

</head>
<body>
	<div id = "header">
			<div id="driver_home">
				<?php
					session_start();
					echo 'Hi, ' . $_SESSION['SESS_FIRST_NAME'] . ' ' . $_SESSION['SESS_LAST_NAME'];
				 ?>
			</div>
			<a id="driver" href="log2.php">Become a Driver
			</a>
			<a id="driver" href="logout.php">Log Out
			</a>
	</div>
	<div id="logo">
		WELCOME TO SCU CARPOOL
	</div>

	<div id="searchbar">
		<form id="search" action="search_result.php" method="post">
			<input class="inputs" type="text" name="start" placeholder="Departure" required=""/>
			<input class="inputs" type="text" name="end" placeholder="Destinition" required="" />
<!-- 			<input class="inputs" type="text" placeholder="Enter Date" required=""/> -->
			<input class="inputs" type="text" name="daytime" placeholder="Enter Time" required=""/>
			<input class="inputs" type="text" name="guest_num" placeholder="Guests" required=""/>
			<input id="button" type="submit" value="Search" />
		</form>
	</div>



</body>

</html>
