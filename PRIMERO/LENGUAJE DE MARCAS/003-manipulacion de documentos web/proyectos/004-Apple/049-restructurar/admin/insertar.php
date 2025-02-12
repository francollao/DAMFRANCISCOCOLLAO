<?php


    include "error.php";
    include "config.php";

    $peticion = "SELECT * FROM ".$_GET['tabla'];	//selecciono todo de una tabla dinamica
    $resultado = $conexion->query($peticion);	//ejecuto peticion contra bd
?>