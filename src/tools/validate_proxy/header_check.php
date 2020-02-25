<?php

$get_headers = apache_request_headers();

echo $__SERVER['REQUEST_METHOD'] . " " . 
    $__SERVER['REQUEST_URI'] . " " . 
    $__SERVER['SERVER_PROTOCOL'] . "<br/>";

foreach ($get_headers as $header => $value) {
  echo "$header: $value <br/>\n";
}

echo "<br/></br/>Your IP address is " . $__SERVER['REMOTE_ADDR'];

?>
