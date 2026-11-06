secreto = 27
acertado = False
intentos = 0

while not acertado:
    intento = int(input("Adivina el número secreto (1 a 50): "))
    intentos += 1
    
    if intento < secreto:
        print("Más alto")
    elif intento > secreto:
        print("Más bajo")
    else:
        acertado = True

print(f"¡Correcto! Lo lograste en {intentos} intentos")
