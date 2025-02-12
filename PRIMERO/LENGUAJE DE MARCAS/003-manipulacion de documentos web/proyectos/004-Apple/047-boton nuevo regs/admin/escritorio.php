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
					<?php include("inc/menu.php"); ?>
				</ul>
			</nav>
			<section>
				<table>
						<thead>
							<tr>
							<?php include("inc/cabeceras.php"); ?>

							</tr>
						</thead>
						<tbody>
						<?php include("inc/contenido.php"); ?>
						</tbody>

				</table>
				<a href="?formulario=<?php echo $_GET['tabla']?>">
				
					<button id="nuevo">+</button>
			
				</a>
			</section>
		</main>
	</body>
	
</html>

<!--SIGUE EN LENGUAJES DE MARCA Y LUEGO CONTINUA PROGRAMACION CON LA CARPETA 34

CARPTEA 27, LENGUAJES DE MARCAS VIDEOS DEL 11 27 16 EN ADELANTE
-->