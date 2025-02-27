<main>
	<?php 
		require_once __DIR__ . "/../bloque/bloque.php"; 
		$conexion = mysqli_connect(
				"localhost", 
				"proyectoapple", 
				"proyectoapple", 
				"proyectoapple"
			);		
		
			$peticion = "
		SELECT * 
		FROM bloque
		WHERE categoria_nombre = ".$_GET['cat']."
		;";																					// Creo una petición
		//echo $peticion;
		$resultado = mysqli_query($conexion, $peticion);						// Ejecuto la petición contra el servidor
																								// Creo un array vacio
		while($fila = mysqli_fetch_array($resultado, MYSQLI_ASSOC)){		// Para cada uno de los resultados
			if($fila['tipobloque_tipo'] == "1"){
				$bloque = new BloqueCompleto($fila['titulo'], $fila['subtitulo']);
    			echo $bloque->getBloque();
			}else if($fila['tipobloque_tipo'] == "2"){
				$bloque = new BloqueCaja($fila['titulo'], $fila['subtitulo']);
    			echo $bloque->getBloque();
			}
		 }
	
		$bloque1 = new BloqueCompleto("bloque1");
		echo $bloque1 ->getBloque();


		$bloque2 = new BloqueCaja("bloque2","sub2");
		echo $bloque2 ->getBloque();
		

		$bloque3 = new BloqueCaja("bloque3","sub4","aaaaaaaaaaaaa","","","border-radius:25px;
		background: blue;");
		echo $bloque3 ->getBloque();
		


		$bloque4 = new BloqueCaja("bloque4","sub4","aaaaaaaaaaaaa","","",
		["background" => "red",
		"border-radius" => "25px"]);
		echo $bloque4 ->getBloque();
		

	?>
</main>
<style>
	<?php include "categoria.css"?>
</style>