lista = [1, 3, 2, 4]
lista.sort()
lista.reverse()
print(lista)

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)

#----LISTA- modifica
lista = [12, 3, 5, 7]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#----TUPLA não modifica

tupla = (1, 2, 3 ,9)
tupla_animal =  tuple\
    (lista_animais)

print(tupla)
print(len(tupla))
print(tupla_animal)

# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# lista_animais.reverse()
# print(lista_animais)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
# print(sum(lista))
# print(min(lista))
#
# print(max(lista_animais))
# print(min(lista_animais))
#
# if 'lobo' \
#    '' in lista_animais:
#     print('Existe')
# else:
#     print('Não existe')
#     lista_animais.append('lobo')
# print(lista_animais)
#
# lista_animais.remove('elefante')
#
# lista_animais.pop(0)
# nova_lista = lista_animais * 3
# print(nova_lista)



