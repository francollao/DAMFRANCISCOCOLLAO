CREATE TABLE `proyectoapple`.`heroes` (`identificador` INT(255) NOT NULL AUTO_INCREMENT ,
 `titulo` VARCHAR(255) NOT NULL , `texto` VARCHAR(255) NOT NULL ,
  `enlace` VARCHAR(255) NOT NULL , `comprar` VARCHAR(255) NOT NULL , 
  `imagen` MEDIUMBLOB NOT NULL , PRIMARY KEY (`identificador`)) ENGINE = InnoDB;