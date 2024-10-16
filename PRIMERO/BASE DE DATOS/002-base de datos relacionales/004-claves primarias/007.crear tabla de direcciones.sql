CREATE TABLE `miempresa`.`direcciones` (`id` INT(10) NOT NULL AUTO_INCREMENT ,
 `calle` VARCHAR(100) NOT NULL , `codigopostal` VARCHAR(50) NOT NULL , 
 `pais` VARCHAR(50) NOT NULL , `empleados_nombre` INT(10) NOT NULL ,
 PRIMARY KEY (`id`)) ENGINE = InnoDB;