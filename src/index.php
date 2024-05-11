<?php
$servername = "localhost";
$username = "root";
$password = "root";
$conn = new mysqli($servername, $username, $password, 'CSSEC');
if ($conn->connect_error) {
    die("数据库连接失败: " . $conn->connect_error);
} 
echo "数据库连接成功";

phpinfo();
