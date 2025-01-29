CREATE DATABASE practicaprog;

-- Crear el usuario y asignarle una contraseña
CREATE USER 'practicaprog'@'localhost' IDENTIFIED BY 'praticaprog';

-- Otorgar todos los privilegios sobre la base de datos al usuario
GRANT ALL PRIVILEGES ON practicaprog.* TO 'practicaprog'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE `practicaprog`.`clientes` (`id` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `apellidos` VARCHAR(255) NOT NULL , `mail` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `practicaprog`.`productos` (`id` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR (255) , `descripcion` TEXT NOT NULL , `precio` DECIMAL(20,2) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;


INSERT INTO `clientes` (`nombre`, `apellidos`, `mail`) VALUES
('Juan', 'Pérez Gómez', 'juan.perez@example.com'),
('María', 'López Fernández', 'maria.lopez@example.com'),
('Carlos', 'Sánchez Ruiz', 'carlos.sanchez@example.com'),
('Laura', 'Hernández Martínez', 'laura.hernandez@example.com'),
('José', 'Martín Torres', 'jose.martin@example.com'),
('Ana', 'García Morales', 'ana.garcia@example.com'),
('Luis', 'Rodríguez Vázquez', 'luis.rodriguez@example.com'),
('Carmen', 'Jiménez Ortega', 'carmen.jimenez@example.com'),
('Miguel', 'Alonso Castro', 'miguel.alonso@example.com'),
('Elena', 'Vargas Blanco', 'elena.vargas@example.com'),
('Sofía', 'Domínguez Soto', 'sofia.dominguez@example.com'),
('Andrés', 'Ortega Ramos', 'andres.ortega@example.com'),
('Lucía', 'Navarro Gil', 'lucia.navarro@example.com'),
('Roberto', 'Iglesias León', 'roberto.iglesias@example.com'),
('Clara', 'Crespo Serrano', 'clara.crespo@example.com'),
('Javier', 'Rojas Núñez', 'javier.rojas@example.com'),
('Patricia', 'Paredes Dávila', 'patricia.paredes@example.com'),
('Francisco', 'Luna Vega', 'francisco.luna@example.com'),
('Isabel', 'Mendoza Cabrera', 'isabel.mendoza@example.com'),
('Fernando', 'Romero Valle', 'fernando.romero@example.com');


#añado inserts de productos

INSERT INTO `productos` (`nombre`, `descripcion`, `precio`) VALUES
('Camiseta básica', 'Camiseta de algodón 100%, disponible en varios colores.', 9.99),
('Jeans ajustados', 'Pantalones vaqueros de corte slim fit, azul clásico.', 29.99),
('Chaqueta de cuero', 'Chaqueta de cuero sintético, estilo biker.', 59.99),
('Vestido de verano', 'Vestido ligero con estampado floral.', 24.99),
('Camisa formal', 'Camisa blanca de manga larga, ideal para oficina.', 19.99),
('Pantalón chino', 'Pantalón casual de tela suave, corte recto.', 34.99),
('Falda plisada', 'Falda midi con pliegues, estilo clásico.', 17.99),
('Zapatillas deportivas', 'Zapatillas ligeras y cómodas para uso diario.', 49.99),
('Abrigo largo', 'Abrigo de lana, ideal para el invierno.', 79.99),
('Gorra deportiva', 'Gorra ajustable con visera curva, diseño minimalista.', 14.99),
('Shorts casuales', 'Pantalones cortos de algodón, ideales para verano.', 12.99),
('Suéter de punto', 'Suéter grueso con diseño de trenzado.', 39.99),
('Blusa estampada', 'Blusa de poliéster con estampado moderno.', 21.99),
('Cinturón de cuero', 'Cinturón negro ajustable con hebilla metálica.', 15.99),
('Chaqueta impermeable', 'Chaqueta ligera y resistente al agua.', 49.99),
('Botas de montaña', 'Botas resistentes con suela antideslizante.', 89.99),
('Bufanda de lana', 'Bufanda cálida, disponible en varios colores.', 11.99),
('Traje de baño', 'Traje de baño de dos piezas, estilo deportivo.', 19.99),
('Calcetines térmicos', 'Calcetines largos y cálidos para invierno.', 8.99),
('Guantes de cuero', 'Guantes elegantes para clima frío.', 29.99);
####insertar categorias 
CREATE TABLE `practicaprog`.`categorias` (`id` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

INSERT INTO `categorias` (`nombre`) VALUES
('Camisetas'),
('Pantalones'),
('Vestidos'),
('Faldas'),
('Chaquetas'),
('Zapatillas'),
('Ropa deportiva'),
('Ropa interior'),
('Sudaderas'),
('Accesorios');