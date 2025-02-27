console.log("soy el js de la cabecera")
let secciones = [
    'Stroe',
    'iMac' ,
    'iPad' ,
    'iPhone'

]

let cabecera = document.querySelector("header nav ul")
let plantilla = document.querySelector("#elmenu")
secciones.forEach(function(seccion) {
    let instancia = plantilla.content.cloneNode(true)
    instancia.querySelector("a").textContent=seccion
    cabecera.appendChild(instancia)
}

)