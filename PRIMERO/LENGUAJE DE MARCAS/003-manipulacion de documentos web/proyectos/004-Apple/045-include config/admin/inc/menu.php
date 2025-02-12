<?php

	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(E_ALL);
	include '../error.php';
	include '../config.php';

	$conexion = new mysqli($servidor, $usuario, $contrasena, $base);

	$peticion = "SHOW TABLES in proyectoapple";
	$resultado = $conexion->query($peticion);

	while ($fila = $resultado->fetch_assoc()) {
		echo "<li><a href='?tabla=".$fila['Tables_in_proyectoapple']."'>".$fila['Tables_in_proyectoapple']."</a></li>";
	}