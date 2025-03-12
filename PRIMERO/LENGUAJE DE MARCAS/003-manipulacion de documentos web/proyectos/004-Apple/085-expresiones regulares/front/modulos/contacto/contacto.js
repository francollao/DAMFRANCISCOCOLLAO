document.querySelector("#enviar").onclick = function(){
	console.log("Voy a ver si envío un mensaje")

	// Primero recojo los datos de los campos del formulario
	let nombre = document.querySelector("#nombre").value
	let email = document.querySelector("#email").value
	let asunto = document.querySelector("#asunto").value
	let mensaje = document.querySelector("#mensaje").value

	let envias = true;

	if (nombre ==""){
		document.querySelector("#nombre").classList.add("rojo")
		document.querySelector("#ayudanombre").textContent="no puedes dejar este campo vacio ";
		envias = false
	}else{
		document.querySelector("#ayudanombre").textContent ="";
		document.querySelector("#nombre").classList.remove("rojo")
	}
//

	if (email ==""){
		document.querySelector("#email").classList.add("rojo")
		document.querySelector("#ayudaemail").textContent="no puedes dejar este campo vacio ";
		envias = false
	}		
	else{
		let reg = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
		if(reg.test(email)){
			document.querySelector("#ayudaemail").textContent = ""
			document.querySelector("#email").classList.remove("rojo")
		}else{
			document.querySelector("#ayudaemail").textContent = "Introduce un email VALIDO"
			document.querySelector("#email").classList.add("rojo")
			envias = false
		}
	}


	if (asunto ==""){
		document.querySelector("#ayudaasunto").textContent="no puedes dejar este campo vacio ";
		document.querySelector("#asunto").classList.add("rojo")
		envias = false
	}else{
		document.querySelector("#ayudaasunto").textContent ="";
		document.querySelector("#asunto").classList.remove("rojo")
	}


	if (mensaje == ""){
		document.querySelector("#ayudamensaje").textContent="no puedes dejar este campo vacio ";
		document.querySelector("#mensaje").classList.add("rojo")
		envias = false
	}else{
		document.querySelector("#ayudamensaje").textContent ="";
		document.querySelector("#mensaje").classList.remove("rojo")
	}



	// Construyo el paquete que voy a enviar
	if(envias==true){
		let paquete = {
			"nombre":nombre,
			"email":email,
			"asunto":asunto,
			"mensaje":mensaje
		}
		console.log(paquete);
	}else{
		console.warn("aun no se ha enviado")

	}

}