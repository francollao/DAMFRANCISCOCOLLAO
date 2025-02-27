fetch("../back/?tabla=carrusel")
    .then(function(response) {
        return response.json();
    })
    .then(function(datos) {
        console.log(datos); // Para ver los datos obtenidos en la consola
        let contenedorCarrusel = document.querySelector("#carrusel1"); // Contenedor del carrusel
        let plantillaCarrusel = document.querySelector("#plantilla-carrusel"); // Plantilla de artículos
        let plantillaBotonera = document.querySelector("#plantilla-botonera"); // Plantilla de puntos
        let botonera = document.querySelector("#botonera"); // Contenedor de puntos

        if (!botonera) {
            console.error("No se encontró el contenedor de la botonera");
        }

        // Duplicar los artículos al inicio y al final para efecto infinito
        let totalArticulos = datos.length;
        let articulos = [];

        datos.forEach(function(dato, index) {
            // Clonamos la plantilla para cada artículo
            let articulo = plantillaCarrusel.content.cloneNode(true);
            articulo.querySelector("h3").textContent = dato.titulo;
            articulo.querySelector("button").textContent = dato.boton;

            let elementoArticulo = articulo.querySelector("article");
            elementoArticulo.style.backgroundImage = "url(data:image/png;base64," + dato.imagen + ")";
            elementoArticulo.style.backgroundSize = "50%";
            elementoArticulo.style.backgroundRepeat = "no-repeat";
            elementoArticulo.style.backgroundPosition = "center";

            // Agregamos el artículo al carrusel
            contenedorCarrusel.appendChild(articulo);
            articulos.push(elementoArticulo);

            // Clonamos la plantilla de la botonera y la agregamos
            let punto = plantillaBotonera.content.cloneNode(true);
            if (punto) {
                botonera.appendChild(punto);
            } else {
                console.error("No se pudo clonar la plantilla del punto");
            }
        });

        // Duplicamos los primeros y últimos artículos para efecto infinito
        let primerArticulo = articulos[0].cloneNode(true);
        let ultimoArticulo = articulos[totalArticulos - 1].cloneNode(true);
        contenedorCarrusel.appendChild(primerArticulo);
        contenedorCarrusel.insertBefore(ultimoArticulo, contenedorCarrusel.firstChild);

        // Variables para manejar el desplazamiento
        let indiceActual = 1; // Comenzamos en el primer artículo real (después del duplicado)
        let desplazamiento = 1024; // Tamaño de cada artículo
        let animacionActiva = true;

        // Configuración inicial para efecto infinito
        contenedorCarrusel.style.left = `-${desplazamiento}px`;
        // Función de animación infinita
        function moverCarrusel() {
            if (animacionActiva) {
                indiceActual++;
                contenedorCarrusel.style.transition = "all 1s ease";
                contenedorCarrusel.style.left = `-${indiceActual * desplazamiento}px`;

                setTimeout(() => {
                    if (indiceActual >= totalArticulos + 1) {
                        indiceActual = 1;
                        contenedorCarrusel.style.transition = "none";
                        contenedorCarrusel.style.left = `-${desplazamiento}px`;
                    }
                }, 1000);
            }
        }

        // Iniciar animación automática cada 3 segundos
        let intervalo = setInterval(moverCarrusel, 3000);
        let timeoutReinicio; // Variable para almacenar el timeout

        // Función para reiniciar la animación después de un tiempo
        function reiniciarAnimacion() {
            clearTimeout(timeoutReinicio); // Evita reinicios múltiples
            clearInterval(intervalo);
            animacionActiva = true;
            intervalo = setInterval(moverCarrusel, 3000);
        }

        // Funcionalidad de puntos de la botonera
        let puntos = document.querySelectorAll(".punto");
        puntos.forEach(function (punto, index) {
            punto.onclick = function () {
                clearInterval(intervalo); // Detiene la animación automática
                animacionActiva = false;

                contenedorCarrusel.style.transition = "all 1s ease";
                indiceActual = index + 1;
                contenedorCarrusel.style.left = `-${indiceActual * desplazamiento}px`;

                // Evita múltiples reinicios y establece un nuevo tiempo de espera
                clearTimeout(timeoutReinicio);
                timeoutReinicio = setTimeout(reiniciarAnimacion, 5000);
            };
        });
    })
    