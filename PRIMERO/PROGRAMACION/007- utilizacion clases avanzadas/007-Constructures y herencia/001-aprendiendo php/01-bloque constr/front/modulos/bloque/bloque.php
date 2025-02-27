<?php 


	function bloque($tipo,$contenido,$estilo){

		$cadena= "<div class ='".$tipo."'style = '".$estilo."'>";
		$cadena .= $contenido;
		$cadena .= "</div>";

		return $cadena;
	}

	//bloque reutilizable 





?>

<style>
	<?php include "bloque.css"?>
</style>


<script>
	<?php include "bloque.js"?>
</script>