
def seleccionar_opcion_menu():
    opciones_menu = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    descripciones_menu = ['Cargar nueva venta', 'Cargar nueva categoría', 'Mostrar ventas por día', 'Mostrar total ingresos', 'Mostrar total productos vendidos', 'Mostrar promedio de ingreso por día', 'Salir']

    for i in range(len(opciones_menu)):
        print(f'{opciones_menu[i]}: {descripciones_menu[i]}')

    opcion = input("Ingrese una opción: ").upper()
    while opcion not in opciones_menu:
        opcion = input(f"Por favor, seleccione una opción valida: ").upper()

    return opcion


def main():
    
    opcion = seleccionar_opcion_menu()
    
    while opcion != 'G':
        if opcion == 'A':
            print(f'{opcion}')
        elif opcion == 'B':
            print(f'{opcion}')
        elif opcion == 'C':
            print(f'{opcion}')
        elif opcion == 'D':
            print(f'{opcion}')
        elif opcion == 'E':
            print(f'{opcion}')
        elif opcion == 'F':
            print(f'{opcion}')

        opcion = seleccionar_opcion_menu()


main()


