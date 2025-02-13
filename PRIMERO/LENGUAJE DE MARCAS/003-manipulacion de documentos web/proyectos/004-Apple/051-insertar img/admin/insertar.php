<?php

	// Este archivo inserta los campos que vienen del formulario

	include "error.php";								// Incluyo los mensajes de error
	
	include "config.php";							// Traigo la conexión a la base de datos
	
	$peticion = "
	INSERT INTO 
	".$_GET['tabla']." 
	VALUES(";											// Arranco una peticion
	
	foreach($_POST as $clave => $valor){		// Para cada uno de los campos del formulario
		if($clave == "Identificador"){			// Si el campo es el identificador
			$peticion .= "NULL,";					// Pon NULL
		}else{											// Pero si es otro campo
			$peticion .= "'".$valor."',";			// pon el valor al campo
		}
	}
	$peticion = substr($peticion, 0, -1);		// quito la ultima coma
	$peticion .= ")									
	";														// cierro peticion
	echo $peticion;									// lanzo la peticion
	$resultado = $conexion->query($peticion);	// la ejecuto
	

											//redirije y en 5 s redirije a la pagina de la url 
?>
   <meta http-equiv="refresh" content="5; url=escritorio.php"> 

