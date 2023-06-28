<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $nombre = $_POST["nombre"];
  $apellido = $_POST["apellido"];
  $telefono = $_POST["telefono"];
  $correo = $_POST["correo"];
  $mensaje = $_POST["mensaje"];

  $to = "laupao41@gmail.com"; // Reemplaza con tu dirección de correo electrónico
  $subject = "Mensaje del formulario de contacto";
  $body = "Nombre: $nombre\nApellido: $apellido\nTeléfono: $telefono\nCorreo: $correo\nMensaje: $mensaje";

  if (mail($to, $subject, $body)) {
    echo "Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.";
  } else {
    echo "Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo.";
  }
}
?>
