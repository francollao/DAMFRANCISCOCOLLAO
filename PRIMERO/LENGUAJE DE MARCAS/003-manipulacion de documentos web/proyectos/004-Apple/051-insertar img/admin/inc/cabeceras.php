<?php
//este archivo carga las cabecera de las tablas 
include "error.php";                //importo la comfigurar de errores

include 'config.php';                 //importo la conexion de base de datos


$peticion = "SHOW COLUMNS FROM  ".$_GET['tabla'];           //quiero todas las columnas de una tabla 
$resultado = $conexion->query($peticion);           //ejecuto la consulta contra la bd

while ($fila = $resultado->fetch_assoc()) {                        //para cada resultado obtenido
  echo "<td>".$fila['Field']."</td>";                             //creo una columna de la tabla
}


$conexion->close();
?>