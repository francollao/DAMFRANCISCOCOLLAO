<?php

// Este archivo inserta los campos que vienen del formulario

include "error.php";  // Incluyo los mensajes de error
include "config.php";  // Traigo la conexión a la base de datos

$peticion = "
INSERT INTO 
".$_GET['tabla']." 
(";  // Empiezo a construir la consulta para las columnas

foreach($_POST as $clave => $valor){  // Para cada uno de los campos del formulario
    if($clave == "Identificador"){  // Si el campo es el identificador
        $peticion .= "Identificador, ";  // Añade la columna 'Identificador'
    } else {  // Para otros campos
        $peticion .= "`".$clave."`, ";  // Añade la columna correspondiente
    }
}

// Verificar si se subió una imagen
if (isset($_FILES['imagen']) && $_FILES['imagen']['error'] == 0) {
    $peticion .= "`imagen`, ";  // Si hay una imagen, añadir la columna 'imagen'
}

$peticion = rtrim($peticion, ", ");  // Eliminar la última coma extra

$peticion .= ") VALUES(";  // Empiezo a añadir los valores

foreach($_POST as $clave => $valor){  // Para cada uno de los campos del formulario
    if($clave == "Identificador"){  // Si el campo es el identificador
        $peticion .= "NULL, ";  // Pon NULL
    } else {  // Para otros campos
        $peticion .= "'".$conexion->real_escape_string($valor)."', ";  // Escapa y agrega el valor
    }
}

// Verificar si se subió una imagen
if (isset($_FILES['imagen']) && $_FILES['imagen']['error'] == 0) {
    $imagen = file_get_contents($_FILES['imagen']['tmp_name']);  // Convierte la imagen a binario
    $imagen = $conexion->real_escape_string($imagen);  // Escapa el contenido
    $peticion .= "'$imagen', ";  // Agregar el valor de la imagen
} else {
    $peticion .= "NULL, ";  // Si no se sube imagen, añadir NULL
}

$peticion = rtrim($peticion, ", ");  // Eliminar la última coma extra
$peticion .= ")";  // Cerrar la consulta

echo $peticion;  // Muestra la consulta para depuración
$resultado = $conexion->query($peticion);  // Ejecuta la consulta

?>
<meta http-equiv="refresh" content="5; url=escritorio.php">