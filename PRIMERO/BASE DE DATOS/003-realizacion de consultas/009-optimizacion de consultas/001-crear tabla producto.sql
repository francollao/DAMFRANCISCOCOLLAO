CREATE TABLE `miempresa`.`productos` (`id` INT(255) NOT NULL AUTO_INCREMENT , 
`nombre` VARCHAR(255) NOT NULL , `descripcion` TEXT NOT NULL ,
 `precio` DECIMAL(10,2) NOT NULL , PRIMARY KEY (`id`)) 
ENGINE = InnoDB;