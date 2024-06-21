import random
import string

def generar_contrasena():
    # Definir conjuntos de caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    # Combinar todos los caracteres
    caracteres = letras_mayusculas + letras_minusculas + digitos + simbolos

    # Generar longitud aleatoria entre 8 y 16 caracteres
    longitud = random.randint(8, 16)

    # Generar contraseña aleatoria usando random.choice
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    return contrasena

# Generar y mostrar la contraseña
contrasena_generada = generar_contrasena()
print(f"La contraseña generada es: {contrasena_generada}")
