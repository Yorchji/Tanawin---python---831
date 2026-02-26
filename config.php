<?php
$host = "localhost";
$user = "std6730202629"; //ชื่อ username ที่จารให้
$pass = "X7m^vT2r"; //รหัสที่จากให้
$db   = "it_std6730202629"; //ชื่อ database

$conn = mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>