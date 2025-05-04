descuento_est = 15
descuento_frecuente = 10
descuento = 0
descuento_aplicado = ""
print("Ingrese el precio del articulo")
precio_inicial = float(input())
print("¿Es estudiante? S/N")
es_estudiante = input().lower() == "s"
print("¿Es cliente frecuente? S/N")
es_frecuente = input().lower() == "s"
if es_estudiante and es_frecuente:
    if descuento_est > descuento_frecuente:
        descuento = descuento_est
        descuento_aplicado = "estudiante"
    elif descuento_frecuente > descuento_est:
        descuento = descuento_frecuente
        descuento_aplicado = "cliente frecuente"
    else:
        descuento = descuento_est
        descuento_aplicado = "estudiante/cliente frecuente"
elif es_estudiante:
    descuento = descuento_est
    descuento_aplicado = "estudiante"
elif es_frecuente:
    descuento = descuento_frecuente
    descuento_aplicado = "cliente frecuente"
else:
    descuento_aplicado = "ninguno"

descuento_m = descuento * precio_inicial / 100
descuento_final = precio_inicial - descuento_m
print(f"Precio inicial: ${precio_inicial:.0f}")
print(f"Descuento aplicado: {descuento}%")
print(f"Descuento total: ${descuento_m:.0f}")
print(f"Precio final: ${descuento_final:.0f}")
if descuento_aplicado == "ninguno":
    print("No se aplicó ningún descuento.")
else:
    print(f"Se aplicó el descuento de {descuento_aplicado}.") 