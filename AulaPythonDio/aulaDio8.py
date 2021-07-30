from aulaDio7_televisao import Televisao
from aulaDio7_calculadora1 import Calculadora
from aula9_conatdor_palavras import contador_letra, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letra(lista))
    print(teste())

