<?php
session_start();
require_once('../php/config.php');

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $name = trim($_POST['name'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if ($name !== '' && $password !== '') {

        // 👑 Admin พิเศษ
        if (strtolower($name) === "tanawin" && $password === "2322546") {

            $_SESSION['user_id'] = 0;
            $_SESSION['name'] = "tanawin";
            $_SESSION['role'] = "admin";

            header("Location: ../pages/show_product.php");
            exit();
        }

        // 👤 ผู้ใช้ทั่วไป
        $stmt = $conn->prepare("SELECT * FROM users WHERE name = ? LIMIT 1");
        if (!$stmt) {
            die("Prepare failed: " . $conn->error);
        }

        $stmt->bind_param("s", $name);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result && $result->num_rows === 1) {

            $user = $result->fetch_assoc();

            if (password_verify($password, $user['password'])) {

                $_SESSION['user_id'] = $user['id'];
                $_SESSION['name'] = $user['name'];
                $_SESSION['role'] = $user['role'];

                header("Location: ../pages/show_product.php");
                exit();
            }
        }

        $error = "Username or Password incorrect!";
        $stmt->close();

    } else {
        $error = "Please fill all fields.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Login</title>
<link rel="stylesheet" href="../allcss/login.css">
</head>
<body>

<div class="login-box">
    <h2>Login</h2>

    <?php if(isset($error)) echo "<p class='error'>$error</p>"; ?>

    <form method="POST">
        <input type="text" name="name" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Sign In</button>
    </form>

    <div style="margin-top:15px;">
        <a href="register.php" class="register-link">Create Account</a>
    </div>
</div>

</body>
</html>