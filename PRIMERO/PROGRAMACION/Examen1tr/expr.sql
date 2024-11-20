-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-11-2024 a las 18:15:54
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
-- Base de datos: `expr`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `capitulos`
--

CREATE TABLE `capitulos` (
  `id` int(255) NOT NULL,
  `capitulo` varchar(255) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `subtitulo` varchar(255) NOT NULL,
  `videourl` varchar(255) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `capitulos`
--

INSERT INTO `capitulos` (`id`, `capitulo`, `titulo`, `subtitulo`, `videourl`, `descripcion`) VALUES
(1, 'I', 'LA ARQUITECTURA', 'De los cimientos a las agujas ', 'https://youtu.be/N-OBoksb9oQ', 'La Catedral de Burgos ha visto pasar 800 años. Generación tras generación, este edificio tan singular ha visto pasar guerras, pandemias, temporales y miles de vidas que han continuado asombrándose con su figura.\r\n\r\nEn el año 1221 se colocó la primera piedra de un proyecto ideado por el Obispo Mauricio y Fernando III el Santo. La nueva catedral, de orden gótico, estaba llamada a sustituir la antigua construcción románica y marcar un hito en el Camino de Santiago y en la historia del arte, inspirándose en las basílicas francesas. La llegada del gótico permitió aligerar los muros y comenzar a construir en altura, buscando el cielo y permitir el paso de la luz.\r\n\r\nEn este primer capítulo, dos profesores de la Universidad de Burgos nos guiarán por las fórmulas de construcción del templo. René Payo y José Matesanz nos introducen en la técnica empleada para levantar las paredes de la catedral, un prodigio científico y tecnológico aún en nuestros días y con la dificultad adicional de los medios empleados por parte de obreros y canteros.\r\n\r\nAdemás, nos adentramos en el Archivo de la seo burgalesa con Matías Vicario, canónigo archivero, para recorrer la memoria de la catedral, con cientos de documentos que no sólo recogen textos eclesiásticos, sino multitud de documentación sobre la vida en la ciudad, la economía, medicina… además de toda la producción documental de la propia Catedral. Una auténtica joya conservada por siglos.\r\n\r\nSin embargo, la construcción de la basílica burgalesa fue todo un desafío que se extendió durante siglos. Las agujas, el cimborrio y algunas de las capillas más emblemáticas son construcciones posteriores que conjugan estilos y técnicas de diferentes épocas. Es precisamente esta unión de estilos, como el gótico, el renacimiento, el barroco y el neoclásico lo que convierte a la catedral de Burgos en un monumento único. Para comprender las particularidades de su construcción, Javier Garabito, arquitecto de la catedral y profesor de la Universidad de Burgos, nos enseña los fundamentos del gótico y la importancia de sus bóvedas, arcos y arbotantes.\r\n\r\nAdemás, la ciencia de la época se basaba, en buena parte, en el ensayo y el error. Prueba de ello fue la caída del cimborrio original ya que, a pesar del enorme conocimiento de los constructores, su técnica podía fallar en ocasiones. Por otro lado, la posición de la seo, construida en cuesta, supone un desafío adicional para su construcción.'),
(2, 'otototottototo', 'tototototo', 'a', 'aaaaaa', 'aaaa'),
(3, '1', 'pepeppeeppepe', 'pepepepepe', 'a', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `capitulos`
--
ALTER TABLE `capitulos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `capitulos`
--
ALTER TABLE `capitulos`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
