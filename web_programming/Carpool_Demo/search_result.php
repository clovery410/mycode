<!DOCTYPE html>
<?php
  session_start();
  $is_driver = $_SESSION['SESS_IS_DRIVER'];

  //Include database connection details
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

  $start = mysqli_real_escape_string($conn, $_POST['start']);
  $end = mysqli_real_escape_string($conn, $_POST['end']);
  $guest_num = mysqli_real_escape_string($conn, $_POST['guest_num']);
  $daytime = mysqli_real_escape_string($conn, $_POST['daytime']);

  if ($start == '') {
    $errmsg_arr[] = 'start missing';
    $errflag = true;
  }
  if ($end == '') {
    $errmsg_arr[] = 'end missing';
    $errflag = true;
  }
  if ($guest_num == '') {
    $errmsg_arr[] = 'guest_num missing';
    $errflag = true;
  }
  if ($daytime == '') {
    $errmsg_arr[] = 'daytime missing';
    $errflag = true;
  }

  //If there are input validations, redirect back to the login form
  // if ($errflag) {
  //   session_write_close();
  //   header("location: publish_route.php");
  //   exit();
  // }


 ?>
<html>
    <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
        <meta charset="utf-8">
        <title>Search Result</title>
        <link rel = "stylesheet" type="text/css" href="css/search_result.css">
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
    <div id="left_section">
        <div id="search_box">
          <div id="search_box_left">
          <form action="search_result.php" method="post">
            <div class="search_box_line">
                <p class="label">Stops</p>
                <div class="search_body">
                    <?php
                      echo '<input type="text" id ="start" name="start" placeholder="Departure" value="' . $start . '" onkeyup="showHint(this.value)">
                            <input type="text" id ="end" name="end" placeholder="Destination" value="' . $end . '" onkeyup="showHint(this.value)">';
                    ?>
                    <!-- <input type="text" id ="start" name="start" placeholder="Departure" value="" onkeyup="showHint(this.value)">
                    <input type="text" id ="end" name="end" placeholder="Destination" value="" onkeyup="showHint(this.value)"> -->
                </div>
            </div>


           <div class="search_box_line">
                <p class="label">Time</p>
                <div class="search_body">
                    <?php
                      echo '<input id="time" type="text" name="daytime" placeholder="00:00" value="' . $daytime . '">
                      <input id ="guests" type="text" name="guest_num" placeholder="Guest Number" value="' . $guest_num . '">';
                    ?>
                    <!-- <input id="time" type="text" name="daytime" placeholder="00:00" value="">
                    <input id ="guests" type="text" name="guest_num" placeholder="Guest Number" value=""> -->
                </div>
           </div>
           <div class="search_box_line">
              <p class="label">REC</p>
              <div class="search_body">
                <p id="recommendation"></p>
              </div>
           </div>
         </div>
         <div id="search_box_right">
            <input id="search_button" type="submit" value="Go!">
         </div>
         </form>
        </div>

        <div id = "search_results">
          <?php
            if (!$errflag) {

              // echo "Your direction after escaping: {$start}<br>";
              // echo "Your area after escaping: {$end}<br>";
              // echo "Your first stop after escaping: {$guest_num}<br>";
              // echo "Your last stop after escaping: {$daytime}<br>";

              //Write search departure and destination to session
              session_regenerate_id();
              $_SESSION['SESS_DEPART'] = $start;
              $_SESSION['SESS_DEST'] = $end;
              session_write_close();

              //Calculate time Limit
              $input_time = strtotime($daytime);
              $upper_time = date("H:i:s", strtotime('+30 minutes', $input_time));
              $lower_time = date("H:i:s", strtotime('-30 minutes', $input_time));
              // $upper_time = strtotime('+30 minutes', $input_time);
              // $lower_time = strtotime('-30 minutes', $input_time);
              // echo $upper_time->format("H:i"), $lower_time->format("H:i");
              // echo 'upper time is: ' . $upper_time . 'lower time is: ' . $lower_time;

              if ($end == 'SCU') {
                $direction = 0;
                $sql = "SELECT Stops.area, Stops.sub_index FROM Stops WHERE Stops.stop_name = '$start'";
              }
              if ($start == 'SCU') {
                $direction = 1;
                $sql = "SELECT Stops.area, Stops.sub_index FROM Stops WHERE Stops.stop_name = '$end'";
              }

              $result = $conn->query($sql);
              $row = $result->fetch_assoc();
              $area = $row['area'];
              $sub_index = $row['sub_index'];

              // //Debug Purpose
              // echo "Your first stop after escaping: {$direction}<br>";
              // echo "Your direction after escaping: {$area}<br>";
              // echo "Your area after escaping: {$sub_index}<br>";

              switch ($sub_index) {
                case 0:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_0, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_0 is not NULL AND Routes.stop_0 >= '$lower_time' AND Routes.stop_0 <= '$upper_time'";
                  break;
                case 1:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_1, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_1 is not NULL AND Routes.stop_1 >= '$lower_time' AND Routes.stop_1 <= '$upper_time'";
                  break;
                case 2:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_2, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_2 is not NULL AND Routes.stop_2 >= '$lower_time' AND Routes.stop_2 <= '$upper_time'";
                  break;
                case 3:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_3, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_3 is not NULL AND Routes.stop_3 >= '$lower_time' AND Routes.stop_3 <= '$upper_time'";
                  break;
                case 4:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_4, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_4 is not NULL AND Routes.stop_4 >= '$lower_time' AND Routes.stop_4 <= '$upper_time'";
                  break;
                case 5:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_5, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_5 is not NULL AND Routes.stop_5 >= '$lower_time' AND Routes.stop_5 <= '$upper_time'";
                  break;
                case 6:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_6, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_6 is not NULL AND Routes.stop_6 >= '$lower_time' AND Routes.stop_6 <= '$upper_time'";
                  break;
                case 7:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_7, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_7 is not NULL AND Routes.stop_7 >= '$lower_time' AND Routes.stop_7 <= '$upper_time'";
                  break;
                case 8:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_8, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_8 is not NULL AND Routes.stop_8 >= '$lower_time' AND Routes.stop_8 <= '$upper_time'";
                  break;
                case 9:
                  $sql = "SELECT route_id, driver_id, user_id, depart, dest, max_people, stop_9, Users.firstname, Users.lastname FROM Routes, Users WHERE Routes.user_id = Users.id AND Routes.region = $area AND Routes.direction = '$direction' AND Routes.max_people >= '$guest_num' AND Routes.stop_9 is not NULL AND Routes.stop_9 >= '$lower_time' AND Routes.stop_9 <= '$upper_time'";
                default:
                  echo "No Match Found";
              }

              $result = $conn->query($sql);

              if ($result->num_rows > 0) {
                //output data of each row
                while ($row = $result->fetch_assoc()) {
                  $route = $row['route_id'];
                  $driver = $row['driver_id'];
                  $user = $row['user_id'];
                  $depart = $row['depart'];
                  $dest = $row['dest'];
                  $maxpeople = $row['max_people'];
                  $firstname = $row['firstname'];
                  $lastname = $row['lastname'];
                  switch ($sub_index) {
                    case 0:
                      $eat = $row['stop_0'];
                      break;
                    case 1:
                      $eat = $row['stop_1'];
                      break;
                    case 2:
                      $eat = $row['stop_2'];
                      break;
                    case 3:
                      $eat = $row['stop_3'];
                      break;
                    case 4:
                      $eat = $row['stop_4'];
                      break;
                    case 5:
                      $eat = $row['stop_5'];
                      break;
                    case 6:
                      $eat = $row['stop_6'];
                      break;
                    case 7:
                      $eat = $row['stop_7'];
                      break;
                    case 8:
                      $eat = $row['stop_8'];
                      break;
                    case 9:
                      $eat = $row['stop_9'];
                      break;
                    default:
                      echo "no result";
                  }

          //         echo '<div class = "search_tag">
          //                  <a class = "select_box" href ="confirmation.php" >
          //                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
          //                      <div class="name">
          //                          <p>' . $firstname, $lastname .'</p>
          //                      </div>
          //                      <form class= "info" action="confirmation.php" method="post">
          //                          <div>
          //                              <p >EAT: </p>
          //                              <p class="eta">' . $eat . '</p>
          //                          </div>
          //                          <div>
          //                              <input class="php_result" name="route_id" value="'. $route . '" />
          //                              <input class="php_result" name="eat" value="'. $eat . '" />
          //                          </div>
          //                          <div>
          //                              <p class="from">' . $depart .'</p>
          //                              <p class="arrow">→</p>
          //                              <p class="to">' . $dest. '</p>
          //                          </div>
          //                          <div>
          //                              <p >Available Seat: </p>
          //                              <p class="eta">' . $maxpeople . '</p>
          //                          </div>
          //                          <input type="submit" value="Detail">
          //                      </form>
          //                  </a>
          //               </div>';
                    echo '<div class="tag">
                          <form action="confirmation.php" method="post">
                          <div class = "search_tag">
                            <div class = "select_box">
                             <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                             <div id="id">' . $firstname. ' ' . $lastname . '</div>

                                 <div>
                                     <p >EAT: </p>
                                     <p class="eta">' . $eat . '</p>
                                 </div>
                                 <div>
                                     <input class="php_result" name="route_id" value="'. $route . '" />
                                     <input class="php_result" name="eat" value="'. $eat . '" />
                                 </div>
                                 <div>
                                     <p class="from">' . $depart .'</p>
                                     <p class="arrow">→</p>
                                     <p class="to">' . $dest. '</p>
                                 </div>
                                 <div>
                                     <p >Available Seat: </p>
                                     <p class="num">' . $maxpeople . '</p>
                                 </div>


                         </div>
                      </div>
                     <input class="b" type="submit" value="Detail">
                    </form>
                   </div>';
                }
              } else {
                echo "Sorry, no match found";
              }
            }
           ?>

            <!-- <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div>

            <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div>

            <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div>

            <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div>

            <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div> -->

            <!-- <div class = "search_tag">
                <a class = "select_box" href ="confirmation.html" >
                    <img class="headShot" src="images/pic.jpg" alt = "HeadShot"/>
                    <div class="name">
                        <p>David Smith</p>
                    </div>
                    <form class= "info">
                        <div>
                            <p >EAT: </p>
                            <p class="eta">14:30</p>
                        </div>
                        <div>
                            <p class="from">Palo Auto</p>
                            <p class="arrow">→</p>
                            <p class="to">SCU</p>
                        </div>
                    </form>
                </a>
            </div> -->
        </div>
    </div>

    <div id="map"></div>
    </div>

    <div id="footer">
        <p id="foot">Copyright@Group2 - Web Programming</p>
    </div>

    <script>
        // function dispear() {
        //   $(".php_result").css("display", "none");
        // }
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
        // load map
        function initMap() {
          var origin = document.getElementById('start').value;
          var destination = document.getElementById('end').value;
          var directionsService = new google.maps.DirectionsService;
          var directionsDisplay = new google.maps.DirectionsRenderer;

          var myCenter=new google.maps.LatLng(37.349650, -121.938934);
          var mapProp = {
            center : myCenter,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          };
          var map=new google.maps.Map(document.getElementById("map"),mapProp);

          var onChangeHandler = function() {
            calculateAndDisplayRoute(directionsService, directionsDisplay);
          };

          if(origin != null && destination != null) {
            calculateAndDisplayRoute(directionsService, directionsDisplay);
          }
          document.getElementById('search_button').addEventListener("click",onChangeHandler);
          // document.getElementById('start').addEventListener('change', onChangeHandler);
          // document.getElementById('end').addEventListener('change', onChangeHandler);
          directionsDisplay.setMap(map);
      }

      function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        if($("#start").val() == "SCU") {
          directionsService.route({
            origin: "500 El Camino Real，Santa Clara, CA 95053",
            destination: document.getElementById('end').value,
            travelMode: google.maps.TravelMode.DRIVING
            }, function(response, status) {
              if (status === google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(response);
              } else {
                window.alert('Directions request failed due to ' + status);
              }
            });
         }
         if($("#end").val() == "SCU") {
           directionsService.route({
             origin: document.getElementById('start').value,
             destination: "500 El Camino Real，Santa Clara, CA 95053",
             travelMode: google.maps.TravelMode.DRIVING
             }, function(response, status) {
               if (status === google.maps.DirectionsStatus.OK) {
                 directionsDisplay.setDirections(response);
               } else {
                 window.alert('Directions request failed due to ' + status);
               }
             });
         }
       }
       // Giving Recomendation for inputs
       function showHint(str) {
        var xhttp;
        if (str.length == 0) {
          document.getElementById("recommendation").innerHTML = "";
          return;
        }
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById("recommendation").innerHTML = xhttp.responseText;
          }
        };
        xhttp.open("GET", "gethint.php?q="+str, true);
        xhttp.send();
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCDu4RXGOHMhpNU-XpOwOkNYCNgj8i4Uc0&signed_in=true&callback=initMap"
        async defer></script>
  </body>
</html>
