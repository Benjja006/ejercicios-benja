kilometro= 0
milla= 0
grado_c= 0
grado_f= 0
print("--------Hola, que conversion deseas?--------")
print("Kilometros a millas (1)")
print("Millas a kilometros (2)")
print("Grados Celcius a Fahrentheit (3)")
print("Grados Fahrentheit (4)")
print("Salir del prohgrama (5)")
opcion = int(input())
while True: 
    if opcion == 1:
        kilometro =int(input("Ingrese kilometros: "))
        if kilometro < 0:
            print("La cantidad no puede ser negativa")
            break
        millas_C= kilometro * 0.621371
        print(f"La cantidad es de: {millas_C} millas ")
        break
    elif opcion == 2:
        milla = int(input("ingrese millas: "))
        if milla < 0:
            print("La cantidad no puede ser negativa")
            break
        kilometro_c= milla * 1.60934
        print (f"La cantidad es de: {kilometro_c} kilometros")
        break
    elif opcion == 3:
        grado_c =int(input("Ingrese grados C°: "))
        grados = grado_c * 9/5 + 32 
        print(f"La cantidad es de: {grados} Grados F")
        if grado_c < 0:
            print("La temperatura está bajo 0")
        elif 15 <= grado_c <= 25:
            print("Está a temperatura ambiente.")
        else:
            print("Hace calor.")
        break
    elif opcion == 4: 
        grado_f =int(input("Ingrese Grados F: "))
        gradoss2= (grado_f - 32) * 5/9
        print(f"La cantidad es de: {gradoss2} Grados C° ")
        if gradoss2  < 0:
            print("Está bajo cero, ¡qué frío!")
        elif 15 <= gradoss2 <= 25:
            print("Está a temperatura ambiente, muy agradable.")
        else:
            print("Hace calor.")
        break
    elif opcion == 5: 
        print("Saliendo del programa, hasta pronto :)")
        break
    else:
     print ("Opcion invalida, intente de nuevo por favor")