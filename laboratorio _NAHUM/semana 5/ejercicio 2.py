# Frase dada
frase = "Soy profesor y me encanta inspirar y enseñar a la gente"

# Dividir la frase en palabras utilizando el método split
palabras = frase.split()

# Crear un conjunto (set) de las palabras únicas
palabras_unicas = set(palabras)

# Contar la cantidad de palabras únicas
cantidad_palabras_unicas = len(palabras_unicas)

print("Número de palabras únicas:", cantidad_palabras_unicas)