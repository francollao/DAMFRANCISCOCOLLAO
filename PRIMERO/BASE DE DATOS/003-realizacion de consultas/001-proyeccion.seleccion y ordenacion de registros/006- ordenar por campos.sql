SELECT 
  id AS ID_Cliente,
  nombre AS Nombre_Cliente,
  email AS Correo_Electronico,
  poblacion AS Ciudad,
  fechadenacimiento AS Fecha_Nacimiento
FROM 
  clientes

ORDER BY nombre;

#se me ha olvidado crear la columna de apellidos jeje