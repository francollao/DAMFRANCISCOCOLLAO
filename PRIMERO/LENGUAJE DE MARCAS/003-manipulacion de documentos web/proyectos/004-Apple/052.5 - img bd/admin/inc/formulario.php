<?php if(isset($_GET['formulario'])){?>
	<h3>Nuevo elemento: <?php echo $_GET['formulario'] ?></h3>
	<form action="insertar.php?tabla= <?php echo $_GET['formulario'] ?>" method="POST"
	enctype="multipart/form-data">
		<?php include "camposform.php"?>
		<input type="submit">
	</form>
	</form>
<?php } ?>