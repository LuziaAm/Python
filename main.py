# This is a Dice Games Python.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

print("Clique 1 para Jogar - Clique em outra tecla para Sair ")
jogar = input("Jogue o Dado: ")


while jogar == "1":
    dado = random.randrange(1, 7)
    print("Número do dado: ", dado)
    jogar = input("Clique 1 para Jogar - Clique em outra tecla para Sair ")
else:
    print("Fim de Jogo")