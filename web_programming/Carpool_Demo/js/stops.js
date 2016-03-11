
var northBayArea = ["San Francisco","Daly City","Millbrae","San Mateo","Redwood City",
                    "Palo Alto","Mountain View","Sunnyvale","Santa Clara","SCU"];
var southBayArea = ["Gilroy","San Martin","Morgan Hill","Coyote","Westfield Oakridge",
                    "Los Gatos","Campbell","Fruitfale","Westfield Valley Fair","SCU"];
var eastBayArea = ["Oakland","Alameda","San Leandro","Hayward","Union City","Fremont",
                   "Newark","Milpitas","San Jose","SCU"];

var area = [northBayArea,southBayArea,eastBayArea];

// Set area select down list to defalut option
function defaultArea() {
  $("#area").empty();
  var option = $("<option>").val("N").text("Please Choose Area");
  var option_0 = $("<option>").val(0).text("North Bay Area");
  var option_1 = $("<option>").val(1).text("South Bay Area");
  var option_2 = $("<option>").val(2).text("East Bay Area");
  $("#area").append(option).append(option_0).append(option_1).append(option_2);

}

// Clear and Set Departure select down list to defalut option
function defaultFrom() {
  $("#from").empty();
  var option = $("<option>").val("N").text("Please Choose Departure");
  $("#from").append(option);

}

// Clear and Set Destination select down list to defalut option
function defaultTo() {
  $("#to").empty();
  var option = $("<option>").val("N").text("Please Choose Destination");
  $("#to").append(option);
}

// Display corresponding stops
function showStops(fromIndex,toIndex) {
  $("#stops").empty();
  if(fromIndex == 9){
    for(i = 8; i >= 0; i--) {
      if(i == toIndex) {
        break;
      }else {
        var display = "<input type='checkbox' class = 'input_checkbox' name = 'stops[]' value=" + i + ">" + areaSelect[i]+ "<br>";
        $("#stops").append(display);
      }
    }
  }
  if(toIndex == 9) {
    count = 0;
    for(i = 0; i < 9; i++) {
      if(i == fromIndex) {
        count = i + 1;
        break;
      }else {continue;}
    }
    for(j = count; j < 9; j++) {
      var display = "<input type='checkbox' class='input_checkbox' name = 'stops[]' value=" + j+ ">" + areaSelect[j] + "<br>";
      $("#stops").append(display);

    }
  }
}
