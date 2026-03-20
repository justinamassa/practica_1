import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6
puntuacion = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    if "_" not in progress:
        print("¡Ganaste!")
        puntuacion += 6
        print(f"Tu puntuacion: {puntuacion}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) !=1 or not letter.isalpha():
        print("Entrada no valida")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntuacion -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntuacion = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print (f"Tu puntuacion: {puntuacion}")