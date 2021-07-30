
lista = [1, 10]
arquivo = ('teste.txt', "r")
try:
    arquivo = open('teste.txt', "r")
    texto = arquivo.read()
    divi = 10 / 1
    numero = lista[0]
    # x = aula

except ZeroDivisionError:
    print('Não é possível dividir por Zero')
except IndexError:
    print('Erro ao acessar um índice inválido')
except Exception as ex: #Grava a mensagem original no EX
    print(ex)
else:
    print('Excuta quando não ocorre exceção')
finally:
    print('Sempre exceuta')
    print('Fechando arquivo')
    arquivo.close()