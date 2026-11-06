corte1 = []
corte2 = []

print("--- NOTAS CORTE 1 ---")
for i in range(4):
    nota = float(input(f"Ingrese la nota del primer corte del estudiante {i + 1}: "))
    corte1.append(nota)

print("\n--- NOTAS CORTE 2 ---")
for i in range(4):
    nota = float(input(f"Ingrese la nota del segundo corte del estudiante {i + 1}: "))
    corte2.append(nota)

print()
for i, (n1, n2) in enumerate(zip(corte1, corte2), start=1):
    promedio = (n1 + n2) / 2
    print(f"Estudiante {i}: promedio {promedio:.2f}")
