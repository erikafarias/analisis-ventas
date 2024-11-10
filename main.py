
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
    #TODO: completar
    return True

def cargar_ventas(ventas):
    categorias = obtener_categorias(ventas)
    print('------------------------------------ \n Cargar nueva venta:')

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
        precio = venta[2]
        cantidad = venta[3]
        total += precio * cantidad
        
    print(f"------------------------------------ \nTotal de ingresos generados: {total}")

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
            print(f'{opcion}')
        elif opcion == 'D':
            calcular_total_ingresos(ventas)
        elif opcion == 'E':
            print(f'{opcion}')
        elif opcion == 'F':
            print(f'{opcion}')

        opcion = seleccionar_opcion_menu()


main()


