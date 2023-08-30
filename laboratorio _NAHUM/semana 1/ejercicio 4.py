# Ejercicio 4: Calcular la serie de Fibonacci hasta el n-ésimo término

n = int(input("Ingrese un número: "))

fibonacci = [0, 1]
while len(fibonacci) < n:
    ultimo = fibonacci[-1]
    penultimo = fibonacci[-2]
    siguiente = ultimo + penultimo
    fibonacci.append(siguiente)

print(fibonacci)
