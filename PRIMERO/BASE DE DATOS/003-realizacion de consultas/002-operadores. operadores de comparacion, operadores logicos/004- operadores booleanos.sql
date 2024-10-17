SELECT 
  nombre AS Nombre_Cliente,
  fechadenacimiento AS Fecha_Nacimiento,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) AS Edad,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) <= 31  `MENOR QUE 31`,
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) <= 31 &&
  TIMESTAMPDIFF(YEAR, fechadenacimiento, CURDATE()) >= 20  AS ` es un joven`
FROM 
  clientes ;
