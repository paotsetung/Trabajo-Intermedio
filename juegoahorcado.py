import random
print("Bienvenido al juego del ahorcado")
def obtener_palabra_aleatoria():
    lista_palabras = ["cadena", "imaginario", "arriba", "cantante", "mantenimiento", "experiencia", "local", "perro"]
    palabra_aleatoria = random.choice(lista_palabras)

import random
print("Bienvenido al juego del Ahorcado!")
def obtener_palabra_aleatoria():
    palabras = ["cadena", "imaginario", "arriba", "cantante", "mantenimiento", "experiencia", "local"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_acertadas): 
    tablero= ""
    for letra in palabra_secreta:
        if letra in letras_acertadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

