<?php
// Array with names
$a[] = "San Francisco";
$a[] = "Daly City";
$a[] = "Millbrae";
$a[] = "San Mateo";
$a[] = "Redwood City";
$a[] = "Palo Alto";
$a[] ="Mountain View";
$a[] ="Sunnyvale";
$a[] ="Santa Clara";
$a[] ="SCU";
$a[]="Gilroy";
$a[] ="San Martin";
$a[] ="Morgan Hill";
$a[] ="Coyote";
$a[] ="Westfield Oakridge";
$a[] ="Los Gatos";
$a[] ="Campbell";
$a[] ="Fruitfale";
$a[] ="Westfield Valley Fair";
$a[] ="Oakland";
$a[] ="Alameda";
$a[] ="San Leandro";
$a[] ="Hayward";
$a[] ="Union City";
$a[] ="Fremont";
$a[] ="Newark";
$a[] ="Milpitas";
$a[] ="San Jose";

// get the q parameter from URL
$q = $_REQUEST["q"];

$hint = "";

// lookup all hints from array if $q is different from ""
if ($q !== "") {
    $q = strtolower($q);
    $len=strlen($q);
    foreach($a as $name) {
        if (stristr($q, substr($name, 0, $len))) {
            if ($hint === "") {
                $hint = $name;
            } else {
                $hint .= ", $name";
            }
        }
    }
}

// Output "no suggestion" if no hint was found or output correct values
echo $hint === "" ? "no suggestion" : $hint;
?>
