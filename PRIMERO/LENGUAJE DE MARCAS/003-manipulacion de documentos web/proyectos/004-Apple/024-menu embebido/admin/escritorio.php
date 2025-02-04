<!doctype html>
<html>
	<head>
		
		<link rel="Stylesheet" href="estilo/escritorio.css">
	</head>
	<body>
		<header></header>
		<main>
			<nav>
				<ul>
					<?php
						$productos = ['iPad','iPhone','iMac','airPods'];
						foreach($productos as $clave=>$valor){
							echo "<li>".$valor."</li>";
						}
					?>
				</ul>
			</nav>
			<section>
			</section>
		</main>
	</body>
</html>