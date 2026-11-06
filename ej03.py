intentos = 0

while True:
    n = int(input("Ingrese un número entero (1 a 10): "))
    intentos += 1
    
    if 1 <= n <= 10:
        break
    
    print("Número fuera de rango")

print(f"Número aceptado: {n} en {intentos} intentos")
