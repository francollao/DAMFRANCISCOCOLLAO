-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2024 a las 19:09:29
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ex bbdd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bibliografia`
--

CREATE TABLE `bibliografia` (      /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `libros` varchar(255) NOT NULL,
  `heore` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `capitulo`
--

CREATE TABLE `capitulo` (      /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `heroe` int(255) NOT NULL,
  `brevetexto` text NOT NULL,
  `capitulo_id` int(255) NOT NULL,
  `imagen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `capitulos`
--

CREATE TABLE `capitulos` (         /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `id_capt` int(255) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `subtitulo` varchar(255) NOT NULL,
  `videourl` varchar(255) NOT NULL,
  `descr` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `creditos`
--

CREATE TABLE `creditos` (          /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `grupo_pertenece` varchar(255) NOT NULL,
  `participantes` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documentacion`
--

CREATE TABLE `documentacion` (       /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `fuente` varchar(255) NOT NULL,
  `imagenes` text NOT NULL,
  `heroe` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `experto`
--

CREATE TABLE `experto` (       /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `heore` int(255) NOT NULL,
  `texto_ex` varchar(255) NOT NULL,
  `nombres_exp` text NOT NULL,
  `id_exper` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `expertos`
--

CREATE TABLE `expertos` (          /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `id_expertos` int(255) NOT NULL,
  `nombre_experto` varchar(255) NOT NULL,
  `funcion` varchar(255) NOT NULL,
  `video` varchar(255) NOT NULL,
  `brevetexto` text NOT NULL,
  `aparece_en` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `heroes`
--

CREATE TABLE `heroes` (    /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `heroe_id` int(255) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `subtitulo` varchar(255) NOT NULL,
  `imagen_fondo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inicio`
--

CREATE TABLE `inicio` (     /* CREAMOS LAS TABLAS Y LE INDICAMOS TANTO COMO SE VA LLAMAR LA COLUMNA Y EL VALOR QUE SE LE VA ASIGNAR, CON EL TIPO DE DATO CORRESPONDIENTE Y LA LONGITUD */
  `titulo` varchar(255) NOT NULL,
  `texto` text NOT NULL,
  `urlvideo` varchar(255) NOT NULL,
  `numero_capt` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bibliografia`
--
ALTER TABLE `bibliografia`
  ADD KEY `heore` (`heore`);

--
-- Indices de la tabla `capitulo`
--
ALTER TABLE `capitulo`
  ADD KEY `capitulo_id` (`capitulo_id`),
  ADD KEY `heroe` (`heroe`);

--
-- Indices de la tabla `capitulos`
--
ALTER TABLE `capitulos`     /* para añadir e indicar que id_capt va ser una llave primaria " PRIMARY KEY "*/
  ADD PRIMARY KEY (`id_capt`);

--
-- Indices de la tabla `documentacion`
--
ALTER TABLE `documentacion`
  ADD KEY `heroe` (`heroe`);

--
-- Indices de la tabla `experto`
--
ALTER TABLE `experto`
  ADD KEY `heore` (`heore`),
  ADD KEY `id_exper` (`id_exper`);

--
-- Indices de la tabla `expertos`
--
ALTER TABLE `expertos`
  ADD PRIMARY KEY (`id_expertos`);

--
-- Indices de la tabla `heroes`
--
ALTER TABLE `heroes`
  ADD PRIMARY KEY (`heroe_id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `bibliografia`
--
ALTER TABLE `bibliografia`
  ADD CONSTRAINT `bibliografia_ibfk_1` FOREIGN KEY (`heore`) REFERENCES `heroes` (`heroe_id`);

--
-- Filtros para la tabla `capitulo`
--
ALTER TABLE `capitulo`
  ADD CONSTRAINT `capitulo_ibfk_1` FOREIGN KEY (`capitulo_id`) REFERENCES `capitulos` (`id_capt`),  /*aqui indicamos donde se unen las tablas mediante sus llaves foraneas y primarias*/
  ADD CONSTRAINT `capitulo_ibfk_2` FOREIGN KEY (`heroe`) REFERENCES `heroes` (`heroe_id`);

--
-- Filtros para la tabla `documentacion`
--
ALTER TABLE `documentacion`
  ADD CONSTRAINT `documentacion_ibfk_1` FOREIGN KEY (`heroe`) REFERENCES `heroes` (`heroe_id`);

--
-- Filtros para la tabla `experto`
--
ALTER TABLE `experto`
  ADD CONSTRAINT `experto_ibfk_1` FOREIGN KEY (`heore`) REFERENCES `heroes` (`heroe_id`),
  ADD CONSTRAINT `experto_ibfk_2` FOREIGN KEY (`id_exper`) REFERENCES `expertos` (`id_expertos`);
COMMIT;

/* POR ULITMO UN COMMIT PARA QUE SE GUARDE TODO */

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



INSERT INTO `capitulos` (`id_capt`, `titulo`, `subtitulo`, `videourl`, `descr`) VALUES ('1', 'LA ARQUITECTUTARA', 'DE LOS CIMIENTOS A LAS AGUJAS', 'https://youtu.be/N-OBoksb9oQ', 'La Catedral de Burgos ha visto pasar 800 años. Generación tras generación, este edificio tan singular ha visto pasar guerras, pandemias, temporales y miles de vidas que han continuado asombrándose con su figura.\r\n\r\nEn el año 1221 se colocó la primera piedra de un proyecto ideado por el Obispo Mauricio y Fernando III el Santo. La nueva catedral, de orden gótico, estaba llamada a sustituir la antigua construcción románica y marcar un hito en el Camino de Santiago y en la historia del arte, inspirándose en las basílicas francesas. La llegada del gótico permitió aligerar los muros y comenzar a construir en altura, buscando el cielo y permitir el paso de la luz.\r\n\r\nEn este primer capítulo, dos profesores de la Universidad de Burgos nos guiarán por las fórmulas de construcción del templo. René Payo y José Matesanz nos introducen en la técnica empleada para levantar las paredes de la catedral, un prodigio científico y tecnológico aún en nuestros días y con la dificultad adicional de los medios empleados por parte de obreros y canteros.\r\n\r\nAdemás, nos adentramos en el Archivo de la seo burgalesa con Matías Vicario, canónigo archivero, para recorrer la memoria de la catedral, con cientos de documentos que no sólo recogen textos eclesiásticos, sino multitud de documentación sobre la vida en la ciudad, la economía, medicina… además de toda la producción documental de la propia Catedral. Una auténtica joya conservada por siglos.\r\n\r\nSin embargo, la construcción de la basílica burgalesa fue todo un desafío que se extendió durante siglos. Las agujas, el cimborrio y algunas de las capillas más emblemáticas
 son construcciones posteriores que conjugan estilos y técnicas de diferentes épocas. Es precisamente esta unión de estilos, como el gótico, el renacimiento, el barroco y el neoclásico lo que convierte a la catedral de Burgos en un monumento único. Para comprender las particularidades de su construcción, Javier Garabito, arquitecto de la catedral y profesor de la Universidad de Burgos, nos enseña los fundamentos del gótico y la importancia de sus bóvedas, arcos y arbotantes.\r\n\r\nAdemás, la ciencia de la época se basaba, en buena parte, en el ensayo y el error. Prueba de ello fue la caída del cimborrio original ya que, a pesar del enorme conocimiento de los constructores, su técnica podía fallar en ocasiones. Por otro lado, la posición de la seo, construida en cuesta, supone un desafío adicional para su construcción.')

/*INSERTAMOS EN LA TABLA CAPITULO LOS SIGUIENTES CAMPOS  : ID_CAPT TITULO ETC Y ACONTINUACION CON VALUES INDICAMOS EL VALOR QUE VA TENER CADA CAMPO DE LA TABLA SEPARADOS POR "," */


/*PENSNADOLO BIEN EN ID_EXPERTO Y ID_CAPITULO DEBERIA HABER PUESTO AUTOINCREMENT , ya que no se van a repetir y son claves primarias */


INSERT INTO `expertos` (`id_expertos`, `nombre_experto`, `funcion`, `video`, `brevetexto`, `aparece_en`) VALUES ('1', 'Itsaso Artetxe', 'Restauradora de arte', 'https://youtu.be/xb_FDmpDKpQ', 'Itsaso Artetxe es restauradora de arte en la empresa Fénix Restauración, especializada en trabajo sobre madera. Lleva varios años trabajando en los bienes muebles de la catedral de Burgos, manteniendo y restaurando los elementos de madera.

La restauradora nos relata cómo la humedad de la catedral puede ser un gran enemigo de los bienes del templo. Junto a Mercedes Chico nos muestra los procesos de restauración y conservación que se llevan a cabo sobre los elementos artísticos de madera y los procesos químicos y físicos que se aplican sobre los mismos. Los procesos deben ser muy delicados y cuidados al detalle, con mucho respeto a las obras, a su valor y su delicado estado.', 'Capítulo IV: La pintura');


/*en la bbdd de php ya tarde para cambiar pero aqui aun a tiempo, no habia visto que habia un breve texto en expertos abajo del video */