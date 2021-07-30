conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}

conjunto = {1, 2, 2, 1, 4, 5}
print(conjunto)
print(conjunto)

conjunto = {10, 20, 30, 40, 50}
conjunto.discard (40)
print(conjunto)

conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)
#NÂO PODE HAVER DUPLICIDADE NO CONJUNTO

# conjunto = {1, 2, 3, 4, 5}
# print(type(conjunto))
# print(conjunto)
# conjunto.add(6)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
conjunto_diferenca1 = conjunto.difference(conjunto2)
print(conjunto_diferenca1)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca2)
conjunto_simetrico = conjunto.symmetric_difference(conjunto2)
print(conjunto_simetrico)

#PERSISTENCE

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)
conjunto_superset =  conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

#conveter lista para conjunto

lista = ['cachorro', 'gato', 'elefante', 'lobo', 'arara', 'gato']

conjunto_animais = set(lista)
print(conjunto_animais)

set_animais = list(conjunto_animais)
print(set_animais)




