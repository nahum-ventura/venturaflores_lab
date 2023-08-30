# Listas de tuplas
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

# Crear conjuntos a partir de las listas
s1 = set(l1)
s2 = set(l2)

# Encontrar elementos comunes entre s1 y s2
s3 = s1.intersection(s2)

# Encontrar elementos únicos para s1 y s2
s4 = s1.symmetric_difference(s2)

# Crear una lista combinada de s3 y s4 ordenada por el número entero de cada tupla
l3 = sorted(list(s3.union(s4)), key=lambda x: x[1])

# Imprimir los resultados
print("Conjunto s1:", s1)
print("Conjunto s2:", s2)
print("Conjunto s3 (elementos comunes):", s3)
print("Conjunto s4 (elementos únicos):", s4)
print("Lista l3 (ordenada por número entero):", l3)