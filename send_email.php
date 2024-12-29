<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Include PHPMailer classes
require 'vendor/autoload.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $mail = new PHPMailer(true);

    try {
        // Server settings
        $mail->isSMTP();                              // Use SMTP
        $mail->Host = 'smtp.gmail.com';               // Set Gmail SMTP server
        $mail->SMTPAuth = true;                       // Enable SMTP authentication
        $mail->Username = 'your-email@gmail.com';     // Your Gmail address
        $mail->Password = 'your-email-password';      // Your Gmail password (or app password if 2FA is enabled)
        $mail->SMTPSecure = 'tls';                    // Encryption type
        $mail->Port = 587;                            // SMTP port for TLS

        // Sender and recipient details
        $mail->setFrom($_POST['email'], 'Form Sender');   // Sender email and name
        $mail->addAddress('recipient@example.com');       // Recipient email

        // Email content
        $mail->isHTML(true);                             // Set email format to HTML
        $mail->Subject = 'Demo Email from PHPMailer';
        $mail->Body    = $_POST['message'];

        // Send the email
        $mail->send();
        echo 'Email sent successfully!';
    } catch (Exception $e) {
        echo "Failed to send email. Error: {$mail->ErrorInfo}";
    }
}
?>
