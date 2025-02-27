
fetch("../back/?tabla=categorias")													// Cargo un endpoint en el back
.then(function(response){														// Cuando obtenga respuesta
	return response.json()														// La conbierto en json
})
.then(function(datos){															// Y cuando reciba datos
	console.log(datos)
	let cabecera = document.querySelector("header nav ul ")
	let plantillamenu = document.querySelector("#elmenu")
	datos.forEach(function(dato){
		/*let instancia = plantillamenu.content.cloneNode(true);
		instancia.querySelector(" li a").textContent = dato.nombre
		cabecera.appendChild(instancia)
*/
		let instancia = plantillamenu.content.cloneNode(true);
		let enlace = instancia.querySelector("a");
		
		enlace.textContent = dato.nombre;
		enlace.setAttribute("href", "categoria.php? cat="+dato.identificador.toLowerCase())
		enlace.setAttribute("cat", dato.identificador.toLowerCase())

		/*instancia.querySelector(" li a").textContent = dato.nombre;

		instancia.querySelector(" li a").setAttribute("href","categoria.php? cat="+dato.nombre.toLowerCase()+".php")*/
		// usa addEventListener para manejar el evento del mouse

		enlace.addEventListener("mouseover", function(){
			console.log("vamos a ver que hay en esta categoria");
			console.log(this.textContent)
			fetch("../back/?busca=productos&campo=categrorias_nombre&dato="+this.getAttribute("cat"))
			.then(function(response){
				return response.json()
			})
			.then(function(datos){
				console.log(datos);


			})
			


		});
	cabecera.appendChild(instancia)




		
	})
})

