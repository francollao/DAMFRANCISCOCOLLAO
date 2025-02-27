<?php


    include "error.php";
    include "config.php";

    $peticion = "INSERT INTO
    ".$_GET['tabla'].
    "VALUES()"
    ;	//selecciono todo de una tabla dinamica
    $resultado = $conexion->query($peticion);	//ejecuto peticion contra bd
?>