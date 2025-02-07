<?php
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', value: 1);
	error_reporting(E_ALL);
	
	$conexion = mysqli_connect(
		"localhost", 
		"proyectoapple", 
		"proyectoapple", 
		"proyectoapple"
	);																						// Me conecto a la base de datos
	$peticion = "SELECT * FROM heroes;";										// Creo una petición
	$resultado = mysqli_query($conexion, $peticion);						// Ejecuto la petición contra el servidor
	$json = [];																			// Creo un array vacio
	while($fila = mysqli_fetch_array($resultado, MYSQLI_ASSOC)){		// Para cada uno de los resultados
		foreach ($fila as $key => $value) {			//REPASAMOS LOS CAMPOS UNO A UNO 							// Repasamos los campos uno a uno
            if (is_string($value) && strlen($value) > 300) { 	    //COMPROBAMOS			// Supongamos que los BLOB son largos
                $fila[$key] = base64_encode($value);						//SI ES PUES QUE NOS LO DEVUELVA EN BASE 64						// Hago un push al array
	    }
    }   
    $json[] = $fila;
    }
	header('Content-Type: application/json');									// El documento va a ser json
   echo json_encode($json);														// SAco el resultado en formato compatible con json
?>