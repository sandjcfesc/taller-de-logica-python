n = int(input("Ingrese la cantidad de números (N > 0): "))
numeros = []

for i in range(n):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

mayor = numeros[0]
contador = 0

for num in numeros:
    if num > mayor:
        mayor = num
        contador = 1
    elif num == mayor:
        contador += 1

print(f"Mayor: {mayor}")
print(f"Aparece {contador} veces")
