<?php

header("Content-Type: text/plain");

if (!isset($_POST['nombre']) || !isset($_POST['email']) || !isset($_POST['asunto']) || !isset($_POST['mensaje'])) {
    echo "Todos los campos son obligatorios.";
    exit;
}

$nombre = htmlspecialchars($_POST['nombre']);
$email = htmlspecialchars($_POST['email']);
$asunto = htmlspecialchars($_POST['asunto']);
$mensaje = htmlspecialchars($_POST['mensaje']);

// Validate email
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "El correo electrónico no es válido.";
    exit;
}

// Compose the email
$to = "franciscojaviercolloacuellar@gmail.com"; // Replace with your recipient email
$subject = "Nuevo mensaje de contacto: $asunto";
$body = "Nombre: $nombre\nEmail: $email\n\nMensaje:\n$mensaje";
$headers = "From: $email\r\nReply-To: $email\r\n";

// Send the email

if (mail($to, $subject, $body, $headers)) {
    echo "El correo se envió correctamente.";
} else {
    echo "Hubo un problema al enviar el correo.";
}
?>