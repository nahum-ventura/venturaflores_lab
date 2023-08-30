import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []

    # Asegurar que haya al menos una letra mayúscula, una minúscula, un número y un carácter especial
    contrasena.append(random.choice(string.ascii_uppercase))
    contrasena.append(random.choice(string.ascii_lowercase))
    contrasena.append(random.choice(string.digits))
    contrasena.append(random.choice(string.punctuation))

    # Generar el resto de caracteres de la contraseña
    for _ in range(longitud - 4):
        contrasena.append(random.choice(caracteres))

    # Mezclar los caracteres para obtener una contraseña aleatoria
    random.shuffle(contrasena)
    
    # Convertir la lista de caracteres en una cadena
    contrasena_str = ''.join(contrasena)
    
    return contrasena_str

def main():
    longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
    
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return
    
    contrasena = generar_contrasena(longitud)
    print("Contraseña generada:", contrasena)

if __name__ == "__main__":
    main()