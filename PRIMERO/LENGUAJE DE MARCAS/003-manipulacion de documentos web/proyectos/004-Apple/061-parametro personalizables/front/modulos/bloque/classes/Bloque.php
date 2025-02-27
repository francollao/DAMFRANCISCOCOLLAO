<?php 

     abstract class Bloque{

        //propiedades variables del objeto
        protected $titulo;
        protected $subtitulo;
        protected $texto;
        protected $imagen;
        protected $imagenfondo;


        /////////// METODOS  ///////////////////////

            //METODO CONSTRUCTOR, LE DA VALORES INICIALES AL OBJETO
            public function __construct(
            $neuvotitulo,
            $nuevosubtitulo = "",
            $nuevotexto = "",
            $nuevaimagen = "",
            $nuevaimagenfondo = "") {
                $this->titulo = $neuvotitulo;
                $this->subtitulo = $nuevosubtitulo;
                $this->texto = $nuevotexto;
                $this->imagen = $nuevaimagen;
                $this->imagenfondo = $nuevaimagenfondo;
    



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

    class BloqueCompleto extends Bloque{

        public function getBloque() {
            return "
            
            <div class='bloque completo'>
            
                <h3>".$this->titulo."</h3>
                <h4>".$this->subtitulo."</h4>
                <p>".$this->texto."</p>

            
            </div>
            ";


        }

}
    class BloqueCaja extends Bloque{

        public function getBloque() {
            return "
            
            <div class='bloque caja'>
            
                <h3>".$this->titulo."</h3>
                <h4>".$this->subtitulo."</h4>
                <p>".$this->texto."</p>

            
            </div>
            ";


        }

    }

?>