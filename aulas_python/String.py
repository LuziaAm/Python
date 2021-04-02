

nome = "Hello World"

print(nome)
print(len(nome))
print(nome[-1])
print(nome[:-1])
print(nome[::-1])
print(nome[::2])

print(nome + ' Concatenar!')
print(nome[10]*10)
print(nome.upper())
print(nome.lower())
print(nome.split())
print(nome.split('W'))

#FORMATAÇÃO
num = 13.5555
print('Numero: %r String: %s ' %(num,'Hi')) # %r e %s transformam qq objeto em string
print('Numero: %s, Valor: %1.2f, String: %s' %(num, 15.89542,'Hi')) # %r e %s transformam qq objeto em string

#string.format

print('Objeto1: {a}, Objeto2: {b}, Objeto3: {c}'.format(a=1,b='two',c=12.3))

print('Objeto2: {b}'.format(b='two'))












