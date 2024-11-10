import datetime

def seleccionar_opcion_menu():
    opciones_menu = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    descripciones_menu = ['Cargar nueva venta', 'Mostrar cantidad de productos vendidos por categoría', 'Mostrar ventas por día', 'Mostrar total ingresos', 'Mostrar cantidad total de productos vendidos', 'Mostrar promedio de ingreso por día', 'Salir'] # eliminar venta?, modificar venta?

    for i in range(len(opciones_menu)):
        print(f'{opciones_menu[i]}: {descripciones_menu[i]}')

    opcion = input("Ingrese una opción: ").upper()
    while opcion not in opciones_menu:
        opcion = input(f"Por favor, seleccione una opción valida: ").upper()

    return opcion

def validar_producto(id):
    while not (1000 <=  id <= 9999):
        id = int(input('Ingrese un código de producto válido. Debe ser un número de cuatro cifras: '))

    return id

def obtener_categorias(ventas):
    categorias = []
    for i in range(len(ventas)):
        if ventas[i][2] not in categorias:
            categorias.append(ventas[i][2])
    
    return categorias

def mostrar_categorias(categorias):
    print('-Categorías: ')
    for i in range(len(categorias)):
        print(f'--{categorias[i]}')

def validar_fecha(fecha):
    if len(fecha) != 10 or fecha[2] != '-' or fecha[5] != '-': #validación del formato de la fecha
        print('El formato de la fecha ingresada no es correcto.')
        return False
    else:
        fecha_lista = fecha.split('-') 
        dia_ingresado = int(fecha_lista[0])
        mes_ingresado = int(fecha_lista[1])
        año_ingresado = int(fecha_lista[2])

        if  1 <= mes_ingresado <= 12: #validación mes entre 1 y 12
            cantidad_dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if not 1 <= dia_ingresado <=  cantidad_dias[mes_ingresado - 1]: # validación cantidad de días por mes, aplica a 2024 u otro año bisiesto
                print('El día ingresado es inválido.')
                return False
            else:
                return True
        else:
            print('El mes ingresado es inválido.')
            return False
        

def cargar_ventas(ventas):
    categorias = obtener_categorias(ventas)
    print('------------------------------------ \nCargar nueva venta:')

    id_venta = ventas[-1][0] + 1 # tomo el último id de venta de la lista y le sumo 1

    id_producto = int(input('Ingrese número del producto: '))
    id_producto = validar_producto(id_producto)

    ver_categorias = input('¿Desea ver las categorías existentes? S/N: ' ).upper()
    if ver_categorias == 'S':
        mostrar_categorias(categorias)
    categoria = input('Ingresar categoría: ')

    precio = float(input('Precio del producto: '))
    precio = round(precio, 2) 

    fecha = input('Ingrese una fecha (en formato dd-mm-aaaa): ')
    while not validar_fecha(fecha):
        fecha = input('Ingrese una fecha (en formato dd-mm-aaaa): ')

    venta = [id_venta, id_producto, categoria, precio, fecha]
    ventas.append(venta)

    return ventas

# Función para obtener el total de los productos vendidos segun la categoria a la que pertenezca 
def calcular_productos_por_categoria(ventas, categoria):
    total_productos = 0
    for venta in ventas:
        if venta[1] == categoria:
            total_productos += venta[3]
    return total_productos

def mostrar_productos_por_categoria(ventas):
    categorias = obtener_categorias(ventas)
    print('------------------------------------ \nMostrar productos vendidos por categoría: ')
    ver_categorias = input('¿Desea ver las categorías existentes? S/N: ' ).upper()
    if ver_categorias == 'S':
        mostrar_categorias(categorias)
    categoria = input('Ingresar categoría: ')
    if categoria not in categorias:
        print('No hay productos para la categoría ingresada.')
    else: 
        cantidad = calcular_productos_por_categoria(ventas, categoria)
        print(f'La cantidad de productos vendidos para la categoría de {categoria} es: {cantidad}')

# Función para obtener el total de los ingresos 
def calcular_total_ingresos(ventas):
    total = 0
    for venta in ventas:
        precio = venta[3]
        cantidad = venta[4]
        total += precio * cantidad     
    print(f"------------------------------------ \nTotal de ingresos generados: {total}")

def filtrar_dias(ventas):
    lista_dias = []
    for venta in ventas:
        if venta[5] not in lista_dias:
            lista_dias.append(venta[5])
    return lista_dias

def filtrar_ventas_por_dia(ventas, dias):
    lista_ventas = []
    for i in range(len(dias)):
        lista_ventas.append([])
        for venta in ventas:
            if venta[5] == dias[i]:
                lista_ventas[i].append(venta)
    return lista_ventas

def imprimir_ventas(lista_ventas):
    for venta in lista_ventas:
        print('   **********')
        print(f'   Id de la venta: {venta[0]}')
        print(f'   Código del producto: {venta[1]}')
        print(f'   Categoría: {venta[2]}')
        print(f'   Precio: {venta[3]}')
        print(f'   Cantidad: {venta[4]}')

def mostrar_ventas_por_dia(ventas):
    print(f"------------------------------------ \nVentas por día")
    opcion = input('¿Qúe desea hacer? \n1- Consultar todas las ventas por día\n2- Consultar ventas de un día en específico\nIngresar opción deseada (1 o 2): ' )
    while not (opcion == '1' or opcion == '2'):
        opcion = input('Ingrese una opción válida: ')
    
    if opcion == '1':
        dias = filtrar_dias(ventas)
    else: 
        dia = input('Ingrese una fecha (en formato dd-mm-aaaa): ')
        while not validar_fecha(dia):
            dia = input('Ingrese una fecha (en formato dd-mm-aaaa): ')
        dias = [dia]
    
    ventas_por_dia = filtrar_ventas_por_dia(ventas, dias)
    for i in range(len(dias)):
        if len(ventas_por_dia[i])>0:
            print('---------------------')
            print(f'Día: {dias[i]}')
            print(f'Ventas: ')
            imprimir_ventas(ventas_por_dia[i])
        else: 
            print('No hay ventas para la fecha ingresada.')


def mostrar_total_productos_vendidos(ventas):
    total = 0
    for venta in ventas:
        total += venta[4] 
    print(f"------------------------------------ \nTotal de productos vendidos: {total}")

def mostrar_promedio_ingresos_por_dia(ventas):
    dias = filtrar_dias(ventas)
    ventas_por_dia = filtrar_ventas_por_dia(ventas, dias)
    suma_promedios = 0

    for i in range(len(dias)):
        suma = 0
        for venta in ventas_por_dia[i]:
            suma += venta[3] * venta[4]
        promedio = suma / len(ventas_por_dia[i])
        suma_promedios += promedio
        print(f'Promedio ingresos {dias[i]}: {promedio}')
    print(f'El promedio total entre los días con ventas es: {suma_promedios / len(dias)}')


#PROGRAMA PRINCIPAL
def main():
    # id de venta, id del producto, categoría, precio, cantidad, fecha
    ventas = [[1, 1000, 'Computación', 800000.00, 1, '01-11-2024'], 
              [2, 3100, 'Celulares', 550000.00, 1, '05-11-2024'], 
              [3, 1000, 'Computación', 800000.00, 1, '03-11-2024'],
              [4, 2150, 'Accesorios de computación', 50000.00, 2, '29-10-2024'],
              [5, 1003, 'Computación', 700000.00, 1, '05-11-2024']]

    opcion = seleccionar_opcion_menu()
    
    while opcion != 'G': # en caso de agregar opciones de menú, modificar
        if opcion == 'A':
            ventas = cargar_ventas(ventas)
        elif opcion == 'B':
            mostrar_productos_por_categoria(ventas)
        elif opcion == 'C':
            mostrar_ventas_por_dia(ventas)
        elif opcion == 'D':
            calcular_total_ingresos(ventas)
        elif opcion == 'E':
            mostrar_total_productos_vendidos(ventas)
        elif opcion == 'F':
            mostrar_promedio_ingresos_por_dia(ventas)
        opcion = seleccionar_opcion_menu()


main()


