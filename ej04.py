operaciones = 0

while True:
    print("\n1. Sumar")
    print("2. Restar")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {n1 + n2}")
        operaciones += 1
    elif opcion == "2":
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {n1 - n2}")
        operaciones += 1
    elif opcion == "0":
        break
    else:
        print("Opción no válida")

print(f"Operaciones realizadas: {operaciones}")
