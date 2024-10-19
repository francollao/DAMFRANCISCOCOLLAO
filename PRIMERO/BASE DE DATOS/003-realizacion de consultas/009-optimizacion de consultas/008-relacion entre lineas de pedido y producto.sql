ALTER TABLE `lineaspedido` ADD CONSTRAINT `lineasaproductos` 
FOREIGN KEY (`producto_nombre`) 
REFERENCES `productos`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;