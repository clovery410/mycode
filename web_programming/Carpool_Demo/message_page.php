<!DOCTYPE html>
<?php
  session_start();
  $is_driver = $_SESSION['SESS_IS_DRIVER'];
  $firstname = $_SESSION['SESS_FIRST_NAME'];
  $lastname = $_SESSION['SESS_LAST_NAME'];
  $email = $_SESSION['SESS_EMAIL'];
  $phone = $_SESSION['SESS_PHONE'];
?>
<html>
    <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
        <meta charset="utf-8">
        <title>Email</title>
        <link rel = "stylesheet" type="text/css" href="css/message_page.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    </head>

    <body>
      <div id = "header">
        <div>
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
        </div>

        <?php
          if ($is_driver == 0) {
            echo '<a id="driver" href="log2.php">Become a Driver
                  </a>';
          } else {
            echo '<a id="driver" href="publish_route.php">Publish a Route
                  </a>';
          }
        ?>
        <!-- <a id="driver" href="logout.php">Log Out
        </a> -->
        <a href="message_page.php">
          <img id="msg" src="images/message.jpg.png" alt="msg" />
        </a>
          <!-- !!!New -->
        <img id="pic" src="images/avatar.jpg" alt="pic"  />
        <span>
          <div id = "slideProfile">
            <div>
              <?php
                echo '<img class="headShot_profile" src="images/pic.jpg" alt = "HeadShot"/>
                <span>' . $firstname . ' ' . $lastname . '</span>
                <p>' . $email . '</p>
                <img id = "star" src = "images/star.png" alt="Rate Star"/>
                <p>Mobile Phone : ' . $phone . '</p>
                <p>500 El Camino, Santa Clara,CA</p>';
              ?>
              <!-- <img class="headShot_profile" src="images/pic.jpg" alt = "HeadShot"/>
              <span>YING TONG</span>
              <p>tongyingkk@gmail.com</p>
              <img id = "star" src = "images/star.png" alt="Rate Star"/>
              <p>Mobile Phone : 650123456</p>
              <p>500 El Camino, Santa Clara,CA</p> -->
            </div>
          </div>
      </span>
    </div>
    <script>
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

      <div class = "section" >
        <h2>Send An Email</h2>
        <form action="mailto:?" method="post" enctype="text/plain">
          Name:<br>
          <input class = "input" type="text" name="name" ><br>
          <!-- Email:<br>
          <input class = "input" type="text" name="email"><br> -->
          Message:<br>
          <input id = "message" type="text" name="message"><br>
          <input class = "button" type="submit" value="Submit">
          <input class = "button" type="reset" value="Reset">
        </form>
    </div>

  </body>
</html>
