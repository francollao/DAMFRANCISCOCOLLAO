fetch("../back/?tabla=carrusel")
.then(function(response){
    return response.json();
})
.then(function(datos){
    console.log(datos); // Para ver los datos obtenidos
    let contenedorCarrusel = document.querySelector("#carrusel1");  // Contenedor del carrusel
    let plantillaCarrusel = document.querySelector("#plantilla-carrusel");  // Plantilla para el artículo
    let plantillaBotonera = document.querySelector("#plantilla-botonera");  // Plantilla para el punto
    let botonera = document.querySelector("#botonera");  // Contenedor de los puntos

    // Verificamos que el contenedor de la botonera está bien
    if (!botonera) {
        console.error("No se encontró el contenedor de la botonera");
    }

    datos.forEach(function(dato, index){
        // Clonamos la plantilla del carrusel para el artículo
        let articulo = plantillaCarrusel.content.cloneNode(true);
        articulo.querySelector("h3").textContent = dato.titulo;  // Añadimos el título
        articulo.querySelector("button").textContent = dato.boton;  // Añadimos el botón
    


        // Ajustamos el fondo del artículo
        let elementoArticulo = articulo.querySelector("article");
        elementoArticulo.style.backgroundImage = "url(data:image/png;base64," + dato.imagen + ")";
        elementoArticulo.style.backgroundSize = "50%";  // Ajusta el tamaño del fondo
        elementoArticulo.style.backgroundRepeat = "no-repeat";  // Evita repetir la imagen
        elementoArticulo.style.backgroundPosition = "center";  // Centra la imagen de fondo

        // Añadimos el artículo al carrusel
        contenedorCarrusel.appendChild(articulo);

        // Ahora clonamos la plantilla del punto y lo agregamos a la botonera
        let punto = plantillaBotonera.content.cloneNode(true);

        // Verificamos que la plantilla del punto se clonó correctamente
        if (punto) {
            botonera.appendChild(punto);  // Añadimos el punto al contenedor de la botonera
            
        } else {
            console.error("No se pudo clonar la plantilla del punto");
        }
        
    });
    let puntos = document.querySelectorAll(".punto");  // Selecciono todos los puntos
    puntos.forEach(function(punto, index){  // Para cada uno de los puntos
        punto.onclick = function(){  // Cuando haga click en un punto
            let carrusel1 = document.querySelector("#carrusel1");  // Cojo el carrusel
            carrusel1.classList.remove("animado1");  // Quito la animación o la quito mejor dicho
            carrusel1.style.marginleft = index * - 1024+"px";
            // Ajusto el desfase en base al punto en el cual he hecho click
            
        }
    });
})
.catch(function(error) {
    console.error("Hubo un problema al cargar los datos:", error);

   
    
});
