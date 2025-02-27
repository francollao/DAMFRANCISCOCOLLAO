<?php
//este archivo carga el contenido interno de las tablas 
	include("error.php");		//cargo la config de errores
	include("config.php");		// cargo la conexion a la base de datos	
	$peticion = "SELECT * FROM ".$_GET['tabla'];	//selecciono todo de una tabla dinamica
	$resultado = $conexion->query($peticion);	//ejecuto peticion contra bd

	while ($fila = $resultado->fetch_assoc()) {
		$identificador = "";		//para cada resultado obtenido
		echo "<tr>";			//comienxo una fila de tabla
		foreach($fila as $clave=>$valor){		//para cada uno de los campos
			if($clave == "identificador"){	//si el campo es menor de 300caracteres
				//echo "<td>".$valor."</td>";		//pongo el valor en la columna
				$identificador = $valor;
			
			}
			if(strlen($valor) < 300){ //si la longitud del valor es menor que 300
				echo "<td>".$valor."</td>";


			}
			
			
			else{								//en caso contrario lo paso a base 64
				echo "<td>
				<img src='data:image/png;base64,".base64_encode($valor)."'>
				</td>";	//cargo los datos como imagen
			}
		}
		echo "
		
		<td> 
			<a href='eliminar.php?tabla=".$_GET['tabla']."&identificador=".$identificador."'> 
				<button class = 'eliminar'> 
			
				x
				</button>
			</a>

		</td>";
			//le pasamos a eliminar php la variable tabla e identificador
		
		//creamos un boton en una nueva columna para cada una de las filas, que nos llevara a la pagina eliminar.php. de la $tabla
	echo "</tr>";	//cierro la fila 
	}


	$conexion->close();		//cierro la conexion a la base de datos
?>