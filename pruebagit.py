minuto = 60
genero_musica = ["rock", "pop", "indie"]
año = 2010
print("Ingrese la duracion de la canción")
duracion_c = float(input())
segundos_c = duracion_c * minuto
print ("Ingrese genero musical")
genero_m = str(input().lower())
print("Escriba el año de lanzamineto")
año_ing = int(input())

fallos = []

if not (150 <= segundos_c <= 270):
    fallos.append("La duración debe estar entre 2.5 y 4.5 minutos.")
if genero_m not in genero_musica:
    fallos.append(f"El género '{genero_m}' no está permitido (rock, pop, indie).")
if not (año_ing >= año):
    fallos.append(f"El año de lanzamiento debe ser posterior a {año}.")

if fallos:
    print("La canción no se añadió a la playlist debido a:")
    for fallo in fallos:
        print(f"- {fallo}")
else:
    print("La canción se añadió a la playlist")