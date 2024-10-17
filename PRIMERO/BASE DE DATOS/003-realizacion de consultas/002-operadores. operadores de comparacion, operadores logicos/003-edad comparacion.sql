SELECT 
  nombre AS Nombre_Cliente,
  fechadenacimiento AS Fecha_Nacimiento,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) AS Edad,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) <= 31 AS `menores de 31`
FROM 
  clientes ;
