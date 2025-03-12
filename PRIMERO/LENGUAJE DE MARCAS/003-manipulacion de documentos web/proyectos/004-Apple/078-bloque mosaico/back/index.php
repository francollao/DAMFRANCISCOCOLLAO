<?php

// Enrutador del back de la apliacion que sirve los datos qyue se piden en funcion de la URL


	include "inc/errores.php";		//configuracion mensajes de error
	include "Classes/ConexionBD.php";	//importo la clase de conexion de BD
	
	header('Content-Type: application/json');		// indico que este archivo devuelve un json

	$conexion = new conexionBD();	// creo un nuevo objeto llamado conexion

	if(isset($_GET['tabla'])){	//si la url me manda una tabla, llamo al metodo correspondiente del objeto
		echo $conexion->pideAlgo($_GET['tabla']);
	}
	if(isset($_GET['busca'])){	//si la url me manda una busqueda
		echo $conexion->buscaAlgo($_GET['busca'],$_GET['campo'],$_GET['dato']);	//llamo al metodo correspondiente del objeto
	}
	
?>
	
	