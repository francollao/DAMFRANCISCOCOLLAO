CREATE TABLE `miempresa`.`clientes` (`id` INT(255) NOT NULL AUTO_INCREMENT , 
`nombre` VARCHAR(100) NOT NULL , 
`email` VARCHAR(100) NOT NULL , 
`poblacion` VARCHAR(100) NOT NULL ,
 `fechadenacimiento` DATE NOT NULL ,
 PRIMARY KEY (`id`)) ENGINE = InnoDB;