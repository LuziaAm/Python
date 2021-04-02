#Listas

my_list = [1,2,3]
print(my_list)
my_list = ['Lu', 23, 100.32, 'List']
print(my_list)
print(len(my_list))

#Indexação e Corte
myList = ['one', 'two', 'three', 4, 5]
print(my_list[0])
print(my_list[1:]) #pega o indice 1 e tudo depois
print(my_list[:3]) #pega tudo até os elementos de indice 3
print(my_list + ['New item']) #concatenar na lista
print(my_list)
my_list = my_list + ['Six']
print(my_list)
print(my_list * 2) #Dobrar a Lista
print(my_list)

#Acrescentar
myList.append('Seis')
print(myList)

#Retirar
myList.pop(4)
print(myList)
item_retirado = myList.pop()
print(item_retirado)
print(myList)
item_retirado = myList.pop()
print(item_retirado)

# REVERTER A ORDEM
nova_lista = ['a','b','c','d','e']
print(nova_lista)

#Revertendo a Lista
print(nova_lista[::-1])
print(nova_lista)

#Usando .reverse
nova_lista.reverse()
print(nova_lista)

# .sort para classificar
nova_lista.sort()
print(nova_lista)










