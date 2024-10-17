SELECT 
  nombre AS Nombre_Cliente,
  fechadenacimiento AS Fecha_Nacimiento,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) AS Edad
FROM 
  clientes ;
