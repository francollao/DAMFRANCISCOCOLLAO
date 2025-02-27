<?php

	// Este archivo inserta los campos que vienen del formulario

	include "../utilidades/error.php";								// Incluyo los mensajes de error
	
	include "../config/config.php";							// Traigo la conexión a la base de datos


$peticion = "INSERT INTO ".$_GET['tabla']." VALUES(";

foreach($_POST as $clave => $valor) {
    if ($clave == 'identificador') {
        $peticion .= "NULL, "; // Si es el identificador, poner NULL
    } else {
        $peticion .= "'".$conexion->real_escape_string($valor)."', ";
    }
}

// Verificar si se subió una imagen
if (isset($_FILES['imagen']) && $_FILES['imagen']['error'] == 0) {
    $imagen = file_get_contents($_FILES['imagen']['tmp_name']);
    $imagen = $conexion->real_escape_string($imagen);
    $peticion .= "'$imagen', "; // Agregar el valor de la imagen
} else {
    $peticion .= "NULL, "; // Si no hay imagen, agregar NULL
}

// Eliminar la última coma extra
$peticion = rtrim($peticion, ", ");
$peticion .= ")";

// Mostrar la consulta para depuración
echo $peticion;

// Ejecutar la consulta
$resultado = $conexion->query($peticion);



?>
   <meta http-equiv="refresh" content="5; url=../escritorio.php"> 

