<?php

	include("config/config.php");		//cargo los datos de conexion

	$peticion = "			
		SELECT * FROM usuarios
		WHERE 
		email = '".$_POST['email']."'
		AND
		contrasena = '".$_POST['contrasena']."'	
		";	//pregunto a la base de datos si hay un usuario y contraseña con esos valores
	$resultado = $conexion->query($peticion);	//hago la peticion y la almaceno en resultado

	if ($fila = $resultado->fetch_assoc()) { //si es cierto que hay un usuario devolvera true y se almacena en fila los datos
											//entonces dejara ir al escritorio 
	  echo '<a href="escritorio.php">Pulsa y vamos al escritorio</a>';
	}else{	// si no hay ningun usuario, no dejara
		echo "Intento de acceso incorrecto";
	}

?>