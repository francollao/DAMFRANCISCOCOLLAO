fetch("../back/?tabla=destacados")													// Cargo un endpoint en el back
.then(function(response){														// Cuando obtenga respuesta
	return response.json()														// La conbierto en json
})
.then(function(datos){															// Y cuando reciba datos
	console.log(datos)
	let contenedordestacados = document.querySelector("#destacados")
	let plantilladestacado = document.querySelector("#plantilladestacado")
	datos.forEach(function(dato){
		let instancia = plantilladestacado.content.cloneNode(true);
		instancia.querySelector("h3").textContent = dato.titulo
		instancia.querySelector("h4").textContent = dato.texto
		/*instancia.querySelector("article").style.background = "url(data:image/png;base64,"+dato.imagen+")"*/
		let article = instancia.querySelector("article");
		article.style.backgroundImage = "url(data:image/png;base64," + dato.imagen + ")";
		article.style.backgroundSize = "50%"; // Ajusta el tamaño al 50% del elemento
		article.style.backgroundRepeat = "no-repeat";
		article.style.backgroundPosition = "center";
		contenedordestacados.appendChild(instancia)
		
	})
})