import random

IMÁGENES_AHORCADO = ['''

   +---+
    |   |
        |
        |
        |
        |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

palabras = "Facil casa agua azul Normal garaje cabeza guardia Dificil curiosidad paracaidas coagulacion".split()

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print("Letras incorrectas: ", end = " ")
    for letra in letrasIncorrectas:
        print(letra, end = " ")
    print()

    espaciosVacios = "_" * len(palabraSecreta)

    # Completar los espacios vacíos con las letras adivinadas.
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
    
    # Mostrar la palabra secreta con espacios entre cada letra.
    for letra in espaciosVacios:
        print(letra, end = " ")
    print()

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra y no otra cosa.
    while True:
        print("Adivina la letra.")
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print("Por favor, introduce una letra.")
        elif intento in letrasProbadas:
            print("Ya has probado esa letra. Elige otra.")
        elif intento not in "abcdefghijklmnñopqrstuvwxyz":
            print("Por favor ingresa una LETRA")
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contratio devuelve False.
    print("¿Quieres jugar de nuevo? (Si o No)")
    return input().lower().startswith("s")

print("A H O R C A D O")
letrasIncorrectas = ""
letrasCorrectas = ""
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
    
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print("¡Sí! ¡La palabra secreta es " + palabraSecreta + "! ¡Has ganado!")
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print("¡Te has quedado sin intentos!\nDespués de " + str(len(letrasIncorrectas)) + " intentos fallidos y " + str(len(letrasCorrectas)) + " aciertos, la palabra era " + palabraSecreta + "")
            juegoTerminado = True
    
    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ""
            letrasCorrectas = ""
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break