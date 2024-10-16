SELECT 
empleados.nombre,
empleados.apellido,
direcciones.calle,
direcciones.codigopostal
FROM
empleados
LEFT JOIN direcciones
ON direcciones.empleados_nombre = empleados.id;