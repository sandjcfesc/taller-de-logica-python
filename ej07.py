n = int(input("Ingrese un número entero N mayor que 0: "))

for fila in range(n):
    for col in range(n):
        if fila == col:
            print(" ", end="")
            continue
        print("*", end="")
    print()
