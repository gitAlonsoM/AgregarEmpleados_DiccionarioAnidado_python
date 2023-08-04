

# Función para agregar un empleado al departamento especificado en el diccionario 'empleados'.
def agregar_empleado(departamento, empleados):
    print(f"\nAgregando empleado al departamento de {departamento}")
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    cargo = input("Cargo del empleado: ")
    clave = input("Clave única del empleado: ")

    # Verificar si la clave ya existe en el departamento
    if clave in empleados[departamento]:
        print(f"Error: Ya existe un empleado con la clave {clave} en el departamento de {departamento}.\n")
    else:
        # Agregar el empleado al departamento correspondiente con su clave única como índice.
        empleados[departamento][clave] = {'nombre': nombre, 'edad': edad, 'cargo': cargo}
        print(f"Empleado agregado correctamente al departamento de {departamento}.\n")




# Función para mostrar todos los empleados en la empresa 
def mostrar_empleados(empleados):
    print("\n==== Empleados en la empresa ====\n")
    
    for departamento, empleados_dept in empleados.items():  # Iterar sobre cada departamento y sus empleados en el diccionario 'empleados'.        
        print(f"==== Departamento: {departamento} ====")
        for clave, empleado_datos in empleados_dept.items(): #iterar sobre clave y datos internos de los empleados de cada departamento
            print(f"ID Empleado: {clave}")
            print(f"Nombre: {empleado_datos['nombre']}")
            print(f"Edad: {empleado_datos['edad']}")
            print(f"Cargo: {empleado_datos['cargo']}")
            print("---------------------------------")



# Eliminar empleado
def eliminar_empleado(departamento, empleados, clave):
    
    if clave in empleados[departamento]:
        del empleados[departamento][clave]
        print(f"Empleado con clave {clave} eliminado del departamento de {departamento}.\n")
    else:
        print("No se encontró ningún empleado con esa clave en el departamento.")




    