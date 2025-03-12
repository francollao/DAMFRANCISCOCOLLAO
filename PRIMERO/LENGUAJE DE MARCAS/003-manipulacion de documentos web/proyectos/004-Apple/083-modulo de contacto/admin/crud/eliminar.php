<?php 
//incluimos la conexion y los mensajes de errores 

include "../utilidades/error.php";
include "../config/config.php";

if (!isset($_GET['tabla']) || empty($_GET['tabla']) || !isset($_GET['identificador']) || empty($_GET['identificador'])) {
    die("Error: Parámetros inválidos.");
}else{
//indicamos la peticion que vamos a usar en este caso DELETE
//se pasan las varuiables tablas e identificador
    $peticion = "

        DELETE FROM ".$_GET['tabla']."
        WHERE identificador = ".$_GET['identificador']."
        ";
        //cerramos consulta
    //eliminamos la tabla donde el identificador es el seleccionado de la tabla
    $resultado = $conexion->query($peticion);   
}


//luego se dirige al escritorio despues de 1s

?>

<meta http-equiv="refresh" content="1; url=../escritorio.php"> 