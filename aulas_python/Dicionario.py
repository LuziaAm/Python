'''
Dicionário em Python:

É um Mapeamento - Coleções de objetos que são armazenados por uma chave

'''
meu_dict = {'key1': 123,'key2': 456, 'key3': [10,20,30]}
print(meu_dict['key1'])
print(meu_dict['key3'])
print(meu_dict['key3'][0])

#novo dicionario
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print(d)
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d)
print(d['key1']['nestkey']['subnestkey'])
e = {'key1': 1, 'key2': 2,'key3':3}
print(e.keys())
print(e.values())
print(e.items())







