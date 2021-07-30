
class Error(Exception):
    pass
class InputError(Error):
    #sempre tem que ter a classe Error
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com um nota de 0 a 10: '))
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #força a exceção
        elif x < 0:
            print('Nota não pode ser menor que zero')
        break
    except ValueError:
        print('Valor inserido inválido, apenas numeros')

    except InputError as ex:
        print(ex)
