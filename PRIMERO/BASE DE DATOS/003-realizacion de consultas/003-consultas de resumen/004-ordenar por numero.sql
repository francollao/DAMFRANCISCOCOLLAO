SELECT 
COUNT(id) AS 'Número de clientes',
poblacion
FROM clientes
GROUP BY(poblacion)
ORDER BY COUNT(Identificador) DESC
;