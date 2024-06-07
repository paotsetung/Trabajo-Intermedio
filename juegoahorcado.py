import random
print("Bienvenido al juego del Ahorcado!")
def obtener_palabra_aleatoria():
    palabras = ["cadena", "imaginario", "arriba", "cantante", "mantenimiento", "experiencia", "local"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_oculta, letras_acertadas):
    tablero= ""
    for letra in palabra_oculta:
        if letra in letras_acertadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)
import random
print("Bienvenido al juego del Ahorcado!")
def obtener_palabra_aleatoria():
    palabras = ["cadena", "imaginario", "arriba", "cantante", "mantenimiento", "experiencia", "local"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_oculta, letras_acertadas):
    tablero= ""
    for letra in palabra_oculta:
        if letra in letras_acertadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado():
    palabra_oculta=obtener_palabra_aleatoria()
    letras_acertadas=[]
    intentos_maximos=6
    intentos=intentos_maximos

    while intentos>0:
        mostrar_tablero(palabra_oculta,letras_acertadas)
        letra=input("Ingrese una letra: ").lower()

        if letra in letras_acertadas:
            print("Prueba otra palabra")
            

        if letra in palabra_oculta:
            letras_acertadas.append(letra)
            if set(letras_acertadas)==set(palabra_oculta):
                print("¡Felicidades! Has adivinado la palabra:", palabra_oculta)
                break

        elif len(letra)==1:
            print("Letra incorrecta. Intentos restantes:", intentos)
            intentos -= 1
        else:
            print(f"Letra incorrecta. Intentos restantes:", intentos)
            intentos -= 1
    # Agregar if antes de intentos, intentos maximos se convirtio en intentos 
    if intentos==0: 
        print("¡Perdiste! La palabra era:", palabra_oculta)
    
# Llamar a la funcion de iniciar juego
jugar_ahorcado()
