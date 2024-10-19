ALTER TABLE `pedidos` ADD CONSTRAINT `pedidos a clientes`
 FOREIGN KEY (`cliente_nombre`) REFERENCES `clientes`(`id`) 
 ON DELETE RESTRICT 
 ON UPDATE RESTRICT;