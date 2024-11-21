''''
cd -- para dirigirte 
ls para listar
sudo apt install 'poner la app'
apache2
php
mysq-server
php-mysqli

 sudo mysql_secure_installation 

 users n
 login remote n
 test database n
 privil y

 ir a directorio html y 'sudo mkdir woordpress' para crear carpeta 

wget para descargar 
enlace wp: https://es.wordpress.org/latest-es_ES.zip

instalar unzip 
y luego sudo unzip nombre del zip

sudo apt install php-mysqli

sudo chmod 777 -R wordpress para dar todos los permisos a la carpera

ahora crear base de datos

sudo mysql -u root -p // para entrar a sql y poder crear la tabla ususario y demas

CREATE DATABASE wordpress;
USE wordpress;
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'wordpress';

GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost'; //GARANTIZAR TODOS LOS PRIVILEGIOS

FLUSH PRIVILEGES; //RECARAGR PRIVILEGIOS

EXIT :)















'''