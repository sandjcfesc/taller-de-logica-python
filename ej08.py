nombres = []

for i in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

for i, nombre in enumerate(nombres, start=1):
    print(f"{i}. {nombre}")
