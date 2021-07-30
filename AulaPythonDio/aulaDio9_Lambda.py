contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cão', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b

print(soma(3,4))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'divi': lambda a, b: a / b
}

soma = calculadora['soma']
subtracao = calculadora['sub']
multiplicacao = calculadora['mult']
divisao = calculadora['divi']

print('Soma é: {}'.format(soma(10, 2)))
print(subtracao(10, 2))
print(multiplicacao(10, 2))
print(divisao(10, 2))