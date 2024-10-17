SELECT 
COUNT(id) AS num_clientes,
poblacion
FROM clientes
GROUP BY poblacion

ORDER BY poblacion ASC;
