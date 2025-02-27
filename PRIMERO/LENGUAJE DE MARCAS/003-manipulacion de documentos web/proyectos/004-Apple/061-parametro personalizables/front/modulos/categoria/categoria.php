<main>
	<?php 
		require_once __DIR__ . "/../bloque/bloque.php"; 
	
		$bloque1 = new BloqueCompleto("bloque1");
		echo $bloque1 ->getBloque();


		$bloque2 = new BloqueCaja("bloque2","sub2");
		echo $bloque2 ->getBloque();
		

		$bloque3 = new BloqueCaja("bloque3","sub4","aaaaaaaaaaaaa");
		echo $bloque3 ->getBloque();
		


		$bloque4 = new BloqueCompleto("bloque4","sub4","aaaaaaaaaaaaa","","");
		echo $bloque4 ->getBloque();
		

	?>
</main>
<script>
	<?php include "categoria.js"?>
</script>
<style>
	<?php include "categoria.css"?>
</style>