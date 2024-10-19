ALTER TABLE `pedidos` ADD CONSTRAINT `pedidosaclientes` 
FOREIGN KEY (`clientes_nombre`) 
REFERENCES `clientes`(`id`) 
ON DELETE RESTRICT ON UPDATE RESTRICT;