# carga de datos
ventas = [
    [1, "Electrónica", 120.5, 3, "01-01-2023"],
    [2, "Ropa", 50.0, 2, "01-01-2023"],
    [3, "Hogar", 200.0, 1, "02-01-2023"],
    [4, "Electrónica", 75.0, 5, "03-01-2023"],
    [5, "Ropa", 30.0, 4, "04-01-2023"],
    [6, "Hogar", 150.0, 2, "05-01-2023"],
    [7, "Electrónica", 99.99, 1, "06-01-2023"],
    [8, "Ropa", 45.0, 6, "06-01-2023"],
    [9, "Hogar", 85.0, 3, "07-01-2023"],
    [10, "Electrónica", 250.0, 2, "08-01-2023"]
]

# Función para obtener el total de los ingresos 
def calcular_total_ingresos(ventas):
    total = 0
    for venta in ventas:
        precio = venta[2]
        cantidad = venta[3]
        total += precio * cantidad
    return total

# Función para obtener el total de los productos vendidos segun la categoria a la que pertenezca 
def calcular_productos_por_categoria(ventas, categoria):
    total_productos = 0
    for venta in ventas:
        if venta[1] == categoria:
            total_productos += venta[3]
    return total_productos

# Función para calcular el promedio de ingresos diario
def calcular_promedio_ingresos_diarios(ventas):
    ingresos_por_dia = {}
    for venta in ventas:
        fecha = venta[4]
        ingreso = venta[2] * venta[3]
        if fecha in ingresos_por_dia:
            ingresos_por_dia[fecha] += ingreso
        else:
            ingresos_por_dia[fecha] = ingreso
    total_ingresos = sum(ingresos_por_dia.values())
    dias = len(ingresos_por_dia)
    promedio = total_ingresos / dias
    return promedio

#Resolver y printear

total_ingresos = calcular_total_ingresos(ventas)
productos_electronica = calcular_productos_por_categoria(ventas, "Electrónica")
productos_ropa = calcular_productos_por_categoria(ventas, "Ropa")
productos_hogar = calcular_productos_por_categoria(ventas, "Hogar")
promedio_ingresos_diarios = calcular_promedio_ingresos_diarios(ventas)

print("Total de ingresos generados:", total_ingresos)
print("Cantidad de productos vendidos en Electrónica:", productos_electronica)
print("Cantidad de productos vendidos en Ropa:", productos_ropa)
print("Cantidad de productos vendidos en Hogar:", productos_hogar)
print("Promedio de ingresos diarios:", promedio_ingresos_diarios)

