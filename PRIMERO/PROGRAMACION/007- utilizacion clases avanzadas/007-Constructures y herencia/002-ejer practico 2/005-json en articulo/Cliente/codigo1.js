window.onload = function(){
	console.log("Javascript funciona")
	fetch("damearticulos.php")
	.then(function(response){
		return response.json()
	})
	.then(function(datos){
		let contenedor = document.querySelector("main")
		datos.forEach(function(dato){
			contenedor.innerHTML += `
				<article>
					<h3>`+dato.titulo+`</h3>
					<time>`+dato.fecha+`</time>
					<p>`+dato.contenido+`</p>
				</article>
			`;
		})
	})
}