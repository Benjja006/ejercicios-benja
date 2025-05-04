biblioteca = ["El Señor de los Anillos", "Fundación", "Dune", "1984", "Un Mundo Feliz"]

while True:
    print("\n--- Biblioteca Digital ---")
    print("1. Ver Libros")
    print("2. Buscar Libro")
    print("3. Agregar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")

    opc = input("Ingrese opción: ")

    if opc == '1':
        if not biblioteca:
            print("Biblioteca vacía.")
        else:
            print("\n--- Libros ---")
            for libro in biblioteca:
                print(f"- {libro}")
            print("-------------\n")
    elif opc == '2':
        buscar = input("Nombre del libro a buscar: ")
        encontrado = False
        for libro in biblioteca:
            if buscar == libro:
                encontrado = True
                break
        if encontrado:
            print(f"\n¡'{buscar}' existe en la biblioteca!\n")
        else:
            print(f"\n'{buscar}' no se encontró en la biblioteca.\n")
    elif opc == '3':
        nuevo = input("Nombre del libro a agregar: ")
        existe = False
        for libro in biblioteca:
            if nuevo == libro:
                existe = True
                break
        if not existe:
            biblioteca.append(nuevo)
            print(f"\n¡'{nuevo}' agregado a la biblioteca!\n")
            if len(biblioteca) > 10:
                print("¡Advertencia! La versión gratuita está llena.\n")
        else:
            print(f"\nEl libro '{nuevo}' ya existe en la biblioteca.\n")
    elif opc == '4':
        eliminar = input("Nombre del libro a eliminar: ")
        existe = False
        indice = -1
        for i, libro in enumerate(biblioteca):
            if eliminar == libro:
                existe = True
                indice = i
                break
        if existe:
            biblioteca.pop(indice)
            print(f"\n¡'{eliminar}' eliminado de la biblioteca!\n")
        else:
            print(f"\n'{eliminar}' no se encontró en la biblioteca.\n")
    elif opc == '5':
        print("¡Gracias por usar la Biblioteca Digital desde Puerto Montt! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")