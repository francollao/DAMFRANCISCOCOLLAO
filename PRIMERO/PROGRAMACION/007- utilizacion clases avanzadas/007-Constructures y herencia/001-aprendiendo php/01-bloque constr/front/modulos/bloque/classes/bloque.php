<?php 

    class Bloque{

        //propiedades variables del objeto
        private $titulo;
        private $subtitulo;
        private $texto;
        private $imagen;
        private $imagenfondo;


        /////////// METODOS  ///////////////////////

            //METODO CONSTRUCTOR, LE DA VALORES INICIALES AL OBJETO
            public function __construct($neuvotitulo,$nuevosubtitulo,$nuevotexto,$nuevaimagen,$nuevaimagenfondo) {
                $this->titulo = $neuvotitulo;
                $this->subtitulo = $nuevosubtitulo;
                $this->texto = $nuevotexto;
                $this->imagen = $nuevaimagen;
                $this->imagenfondo = $nuevaimagen;
    



            }

            //metodos set y get - LEEN Y ESCRIBEN VALORES A LAS PROPIEDADES
            public function getBloque() {
                return "
                
                <div class='bloque'>
                
                    <h3>".$this->titulo."</h3>
                    <h4>".$this->subtitulo."</h4>
                    <p>".$this->texto."</p>

                
                </div>
                ";


            }



}


$bloque1 = new Bloque("titulo1","subtitu2","aaaaaaaaaaaaaaaaaaa",
"","");

echo $bloque1 ->getBloque();

$bloque2 = new Bloque("titulo2","subtitu2","aaaaaaaaaaaaaaaaaaa",
"","");

echo $bloque2 ->getBloque();









?>