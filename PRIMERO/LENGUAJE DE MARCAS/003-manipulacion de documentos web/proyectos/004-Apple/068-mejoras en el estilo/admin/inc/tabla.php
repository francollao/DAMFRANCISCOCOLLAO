<?php if(isset($_GET['tabla'])){?>
	<table>
		<thead>
			<tr>
				<?php include "cabeceras.php"?>
			</tr>
		</thead>
		<tbody>
			<?php include "contenido.php"?>
		</tbody>
	</table>
	<a href="?formulario=<?php echo $_GET['tabla'] ?>">
		<button id="nuevo">+</button>
	</a>
<?php } ?>