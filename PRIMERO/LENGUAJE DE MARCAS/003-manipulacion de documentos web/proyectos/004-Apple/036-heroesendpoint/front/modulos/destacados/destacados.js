console.log("soy el js de los detacados")
let detacados = [ //creo un array de elementos
    'uno',
    'dos' ,
    'tres' ,
    'cuadro',
    'cinco' ,
    'seis'

]

let contenedordestacados = document.querySelector("#destacados") //seleciono un contenedor que dentro se supone esta la plantilla (template)
let plantilladestacados = document.querySelector("#destacado") //selecciono el elemento plantilla 
detacados.forEach(function(detacado) {      //para cada uno de los destacados 
    let instancia = plantilladestacados.content.cloneNode(true) //clono la plantilla 
    instancia.querySelector("h3").textContent=detacado  //cambio el texto de cada instacia en este caso el h3 por cada uno de los elementos del array
    contenedordestacados.appendChild(instancia) //lo añado al contenedor
}


)