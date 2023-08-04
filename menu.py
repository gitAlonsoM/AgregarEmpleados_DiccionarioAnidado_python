from funciones import agregar_empleado, mostrar_empleados, eliminar_empleado

""" 
El algoritmo, basado en un diccionario anidado, permite mediante un menú interactivo: 
agregar empleados con diferentes atributos a distintos departamentos, mostrar la lista de empleados, eliminar empleados por su clave única y salir del menú."""


# Inicializar el diccionario 'empleados' con los tres departamentos y un diccionario vacío para cada uno.
empleados = {
    'Ventas': {},
    'Marketing': {},
    'Tecnología': {}
}


#Menu interactivo
while True:
    print("\n--------Menú -------")
    print("1. Agregar empleado")
    print("2. Visualizar empleados")
    print("3. Eliminar empleado")
    print("4. Salir\n")

    try:
        opcion = int(input("Ingrese una opción : "))

        if opcion == 1:
            print("Departamentos disponibles: \n1 = Ventas\n2 = Marketing\n3 = Tecnología")
            
            departamento_opcion = int(input("Ingrese el número del departamento: "))
            if departamento_opcion == 1:
                agregar_empleado('Ventas', empleados)
            elif departamento_opcion == 2:
                agregar_empleado('Marketing', empleados)
            elif departamento_opcion == 3:
                agregar_empleado('Tecnología', empleados)
            else:
                print("Numero no válido.")

        elif opcion == 2:
            #print(empleados)
            mostrar_empleados(empleados)
            
        elif opcion == 3:
            print("Eliminar empleado")
            print("Departamentos disponibles: \n1 = Ventas\n2 = Marketing\n3 = Tecnología")
            departamento_opcion = int(input("Ingrese el número del departamento: "))
            if departamento_opcion == 1:
                departamento = 'Ventas'
            elif departamento_opcion == 2:
                departamento = 'Marketing'
            elif departamento_opcion == 3:
                departamento = 'Tecnología'
            else:
                print("Número no válido.")
                continue
            
            clave = input("Ingrese la clave única del empleado a eliminar: ")
            eliminar_empleado(departamento, empleados, clave)   
        

        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

    except:
        print("Error: Ingrese un número válido.")
