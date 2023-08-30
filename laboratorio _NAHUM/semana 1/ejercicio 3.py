# Ejercicio 3: Encontrar la factorial de un número

n = int(input("Ingrese un número: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("El factorial de", n, "es:", factorial)

n = int(input("Ingrese un número: "))

