
usuario= "Pepito"
contra= "adictoalfrefire123"
usuarioing= input("Ingrese su usuario: ")
contraing= input("Ingrese contraseña: ")
if usuarioing == usuario and contraing == contra:
    print(f"Bienvenido {usuarioing}")
elif usuarioing == usuario:
    print("Contraseña incorrecta")
    print(f"Pista: la contraseña comienza con '{contra[0]}'")
else:
    print("Usuario no valido.")