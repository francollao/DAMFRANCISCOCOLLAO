let puntos = document.querySelectorAll(".punto")//seleciono los puntos
puntos.forEach(function(punto,index){ //para cada uno de los puntos
	punto.onclick = function(){//cuando haga click en un punto
		let carrusel1= document.querySelector("#carrusel1")//cojo el carrusel
		carrusel1.classList.remove("animado1")//paro la animacion o la quito mejor dicho

		carrusel1.style.left = 0-index *1024+"px"// le pongo a mano el desfase en base al punto en el cual he hecho click
	}
})