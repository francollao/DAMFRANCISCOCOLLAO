<?php
//este archivo carga el contenido interno de las tablas 
	include("error.php");		//cargo la config de errores
	include("config.php");		// cargo la conexion a la base de datos	
	$peticion = "SELECT * FROM ".$_GET['tabla'];	//selecciono todo de una tabla dinamica
	$resultado = $conexion->query($peticion);	//ejecuto peticion contra bd

	while ($fila = $resultado->fetch_assoc()) {		//para cada resultado obtenido
		echo "<tr>";			//comienxo una fila de tabla
		foreach($fila as $clave=>$valor){		//para cada uno de los campos
			if(strlen($valor) < 300){	//si el campo es menor de 300caracteres
				echo "<td>".$valor."</td>";		//pongo el valor en la columna
			}else{								//en caso contrario lo paso a base 64
				echo "<td><img src='data:image/png;base64,".base64_encode($valor)."'></td>";	//cargo los datos como imagen
			}
		}
	echo "</tr>";		//cierro la fila 
	}


	$conexion->close();		//cierro la conexion a la base de datos
?>