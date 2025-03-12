<?php

	$servidor = "localhost";//defino servidore , el usuario, la contraseña y la bd
	$usuario = "proyectoapple";
	$contrasena = "proyectoapple";
	$base = "proyectoapple";

	$conexion = new mysqli($servidor, $usuario, $contrasena, $base);
								//creo una conexion de tipo mysql
?>