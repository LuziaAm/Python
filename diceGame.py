# This is a Dice Games Python.

# Press 1 to start the game.
# Press other key to stop game.
import random

print("Clique 1 para Jogar - Clique em outra tecla para Sair ")
jogar = input("Jogue o Dado: ")


while jogar == "1":
    dado = random.randrange(1, 7)
    print("Número do dado: ", dado)
    jogar = input("Clique 1 para Jogar - Clique em outra tecla para Sair ")
else:
    print("Fim de Jogo")
