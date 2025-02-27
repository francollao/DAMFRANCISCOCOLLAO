
fetch("../back/?tabla=categorias")													// Cargo un endpoint en el back para las categroias
.then(function(response){														// Cuando obtenga respuesta entonces 
	return response.json()														// La conbierto en json 
})
.then(function(datos){															// Y luego  cuando reciba datos 
	console.log(datos)
	let cabecera = document.querySelector("header nav ul ")			//seleciono la cabecera
	let plantillamenu = document.querySelector("#elmenu")		//tomo la plantilla 
	datos.forEach(function(dato){		//para cada dato dato recibido
		/*let instancia = plantillamenu.content.cloneNode(true);
		instancia.querySelector(" li a").textContent = dato.nombre
		cabecera.appendChild(instancia)
*/
		let instancia = plantillamenu.content.cloneNode(true);	//creo y clono una instancia
		let enlace = instancia.querySelector("a");	//seleciono un enlace interior
		
		enlace.textContent = dato.nombre;		//le pongo el atributo de texto
		enlace.setAttribute("href", "categoria.php? cat="+dato.identificador.toLowerCase())	//y le digo a que pagina debe ir
		enlace.setAttribute("cat", dato.identificador.toLowerCase())	//le pongo un atributo a la categoria

		/*instancia.querySelector(" li a").textContent = dato.nombre;

		instancia.querySelector(" li a").setAttribute("href","categoria.php? cat="+dato.nombre.toLowerCase()+".php")*/
		// usa addEventListener para manejar el evento del mouse

		enlace.addEventListener("mouseover", function(){		//caundo paso el mouse por encima de esa categoria
			console.log("vamos a ver que hay en esta categoria");	
			console.log(this.textContent)
			let tituloseccion = this.textContent	//cargo el titulo de la cat
			fetch("../back/?busca=productos&campo=categrorias_nombre&dato="+this.getAttribute("cat")) //fetch para obtener productos por categoria
			.then(function(response){ //cuando tenga la respuesta
				return response.json() 	//lo paso a json
			})
			.then(function(datos){	//luego con los datos recibidos
				console.log(datos);
				document.querySelector("#categoria").textContent = tituloseccion; //pongo el titulo de la categoria
				document.querySelector("#productos").innerHTML = "";	//vacio los productos
				datos.forEach(function(dato){	//para cada dato
					document.querySelector("#productos").innerHTML += "<li><a href ='producto.php?prod="+dato.identificador+"'> "+dato.titulo+"</a></li>"; // creo en productos una lista con el titulo de cada producto


				})


			})
			


		});
	cabecera.appendChild(instancia)




		
	})
})

