<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Publish A Route</title>
  <meta name="description" content="Driver Interface">
  <meta name="author" content="Qianhui Jiang">

  <link rel="stylesheet" href="css/publish_route.css">

  <script src="js/stops.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
</head>

<body>
 <script>
  var areaSelect;
  $(document).ready(function(){
    // Direction Changed
    $("#route").change(function(){
      // Clear and set default for below select down list
      defaultArea();
      defaultFrom();
      defaultTo();
      // If select heading school
      if($("#route").val() == 0) {
        var option = $("<option>").val(9).text("SCU");
        $("#to").append(option);

      }
      // If select leaving shcool
      if($("#route").val() == 1) {
        var option = $("<option>").val(9).text("SCU");
        $("#from").append(option);
      }
    })

    // Area Changed
    $("#area").change(function(){
      if($("#route").val() == 0) {
        defaultFrom();
        var areaIndex = $("#area").val();
        areaSelect = area[areaIndex];
        // Generate corresponding departures
        for(i = 0; i < 9; i++) {
          var option = $("<option>").val(i).text(areaSelect[i]);
          $("#from").append(option);
        }
      }

      if($("#route").val() == 1) {
        defaultTo();
        var areaIndex = $("#area").val();
        areaSelect = area[areaIndex];
        // Generate corresponding destinations
        for(i = 0; i < 9; i++) {
          var option = $("<option>").val(i).text(areaSelect[i]);
          $("#to").append(option);
        }
      }
    })

    // Departure Changed
    $("#from").change(function(){
      var fromIndex = $("#from option:selected").val() ;
      var toIndex = $("#to option:selected").val();
      if(fromIndex != "N" && toIndex != "N") {
        showStops(fromIndex,toIndex);
      }
    })
    // Destination Changed
    $("#to").change(function(){
      var fromIndex = $("#from option:selected").val() ;
      var toIndex = $("#to option:selected").val();
      // $("#publish_title").text("abcde");
      if(fromIndex != "N" && toIndex != "N") {
        // $("#publish_title").text("abcde");
        showStops(fromIndex,toIndex);
       }
     })
   })
  </script>
    <div id = "header">
        <div>
        <a href="driver_home.php">
            <h1 id="scu">SCU</h1>
            <h1 id="carpool">Carpool</h1>
        </a>
        </div>
            <img id="pic" src="images/avatar.jpg" alt="pic" />
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
        <a id="driver" href="publish_route.php">Publish a Route
        </a>
        <a id="driver" href="logout.php">Log Out
  			</a>
    </div>


    <div id="main">
      <form name="publish" action="publish_exec.php" method="post">
        <div id="publish_title">
            <p>Publish Your Route</p>
        </div>
        <div class="steps">
            <div class="step_pic">
                <img id="step1" src="images/step1.png" alt="step1" />
            </div>
            <div class="step_body">
            <p class="category"> Step1: Route</p>
            <div class="input_wrapper">
                <div class="select">
                    <span class="arr"></span>
                    <select id="route" name="direction">
                        <option value="N">Please choose a direction</option>
                        <option value="0">Heading SCU</option>
                        <option value="1">Leaving SCU</option>
                    </select>
                </div>
            </div>

            <div class="input_wrapper">
                <div class="select">
                    <span class="arr"></span>
                    <select id="area" name="area">
                        <option value="N">Please choose Area</option>
                        <option value="0">North Bay Area</option>
                        <option value="1">South Bay Area</option>
                        <option value="2">East Bay Area</option>
                    </select>
                </div>
            </div>
            </div>
        </div>


        <div class="steps">
            <div class="step_pic">
                <img id="step2" src="images/step2.png" alt="step2" />
            </div>
            <div class="step_body">
            <p class="category"> Step2: Stops</p>
            <div class="input_wrapper">
                <div class="select">
                    <span class="arr"></span>
                    <select id="from" name="first_stop">
                        <option value="N">Please Choose Departure</option>
                    </select>
                </div>
            </div>

            <div class="input_wrapper">
                <div class="select">
                    <span class="arr"></span>
                    <select id="to" name="last_stop">
                        <option value="N">Please Choose Destination</option>
                    </select>
                </div>
            </div>

            <div class="input_wrapper">
<!--                 <p id="choose_stops"></p>
                <div id ="stops"></div> -->
                <div class="input_label" id="choose_stops">Please Choose Intermediate Stops</div>
                <div class="input_frame" id="stops"></div>

            </div>
            </div>
        </div>
        <div class="steps">
            <div class="step_pic">
                <img id="step3" src="images/clock.png" alt="step3" />
            </div>
            <div class="step_body">
            <p class="category"> Step3: Time</p>
            <div class="input_wrapper">
                <div class="input_body">
                    <img class="input_icon" src="images/clock.png" alt="LOGO" />
                    <input class="input_textfield" name="time" placeholder="12:30" />
                </div>
            </div>
            </div>
        </div>
        <div class="steps">
            <div class="step_pic">
                <img id="step4" src="images/step4.png" alt="step4" />
            </div>
            <div class="step_body">
            <p class="category"> Step4: Maximum Capacity</p>
            <div class="input_wrapper">
                <div class="input_body">
                    <img class="input_icon" src="images/people.png" alt="LOGO" />
                    <input class="input_textfield" name="max_people" placeholder="4" />
                </div>
            </div>
            <input id="button" type="submit" value="Submit">
            </div>

        </div>
      </form>
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
