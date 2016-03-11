<!DOCTYPE html>
<?php
  //Start session
  session_start();
  //Unset the variables stored in session
  unset($_SESSION['SESS_USER_ID']);
  unset($_SESSION['SESS_FIRST_NAME']);
  unset($_SESSION['SESS_LAST_NAME']);
  unset($_SESSION['SESS_EMAIL']);
  unset($_SESSION['SESS_IS_DRIVER']);
  unset($_SESSION['SESS_PHONE']);
 ?>
 <!DOCTYPE html>
 <html>
 <head>
 	<title>Sign Up/Log In</title>
 	<link href="css/log.css" rel="stylesheet" type="text/css">
 </head>
 <body>
     <div id = "header">
 		<div>
 		<a href="first_page.html">
         	<h1 id="scu">SCU</h1>
         	<h1 id="carpool">Carpool</h1>
         </a>
         </div>
 	</div>

 	<div id="main">
 	<div id="signup">
 		<p class="head">Sign Up</p>
 		<div class="form">
 			<form name="signup_form" action="signup_exec.php" method="post">
 				<div class="label">First Name</div>
 				<input type="text" name="firstname" value=""><br>
 				<div class="label">Last Name</div>
 				<input type="text" name="lastname" value=""><br>
 				<div class="label">Phone</div>
 				<input type="text" name="phone" value=""><br>
 				<div class="label">Email</div>
 				<input type="text" name="email" value=""><br>
 				<div class="label">Password</div>
 				<input type="password" name="newpass" value=""><br>
 				<div class="label">Confirm Password</div>
 				<input type="password" name="confirmpass" value="" onchange="checkPass()"><br>
 				<div class="b">
 					<input class="button" type="submit" value="Sign Up" name="submit">
 				</div>
 			</form>
 		</div>
 	</div>
 	<div id="login">
 		<p class="head">Log In</p>
 		<div class="form">
 			<form name="loginform" action="login_exec.php" method="post">
        <!--the code bellow is used to display the message of the input validation-->
       <?php
        if( isset($_SESSION['ERRMSG_ARR']) && is_array($_SESSION['ERRMSG_ARR']) && count($_SESSION['ERRMSG_ARR']) >0 ) {
        echo '<ul class="err">';
        foreach($_SESSION['ERRMSG_ARR'] as $msg) {
          echo '<li>',$msg,'</li>';
          }
        echo '</ul>';
        unset($_SESSION['ERRMSG_ARR']);
        }
      ?>
 				<div class="label">Email</div>
 				<input type="text" name="email" value=""><br>
 				<div class="label">Password</div>
 				<input type="password" name="password" value=""><br>
 				<div class="b">
 					<input class="button" type="submit" value="Log In">
 				</div>

 			</form>

 		</div>
 	</div>
 	</div>

 	<div id="footer">
 		<p id="foot">Copyright@Group2 - Web Programming</p>
 	</div>
  <script>
    function checkPass() {
      var old_pass = document.getElementById("pass1").value;
      var new_pass = document.getElementById("pass2").value;
      if (old_pass != new_pass) {
        alert("Password does not match");
      }
    }
  </script>
 </body>
 </html>
