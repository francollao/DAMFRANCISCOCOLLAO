console.log("soy el js de la cabecera")
let secciones = [
    'Stroe',
    'iMac' ,
    'iPad' ,
    'iPhone'

]

let cabecera = document.querySelector("header nav ul")
secciones.forEach(function(seccion) {
    cabecera.innerHTML += `
        <li>
			<a href="">`+seccion+`</a>
		</li>

    
    `

}


)