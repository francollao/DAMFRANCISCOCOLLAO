<?php

//este archivo carga las entradas del menu de la izquierda
include("error.php");
include("config.php");


$peticion = "SHOW TABLES in proyectoapple";
$resultado = $conexion->query($peticion);

while ($fila = $resultado->fetch_assoc()) {	//para cada uno de los resultados :
	echo "
	<li>
		<a href='?tabla=".$fila['Tables_in_proyectoapple']."'>".$fila['Tables_in_proyectoapple']."</a>
	</li>";			//pongo un elemento nuevo del menu 
}