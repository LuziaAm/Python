class Calculadora:
    # def __init__(self):
    #     pass
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def sub (self, valor_a, valor_b):
        return valor_a - valor_b
    def mult (self, valor_a, valor_b):
        return valor_a * valor_b
    def divi (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 4))
print(calculadora.sub(20, 14))
print(calculadora.mult(8, 2))
print(calculadora.divi(21, 7))
# print(soma(1, 4))
# print(sub(10, 4))
# print(mult(10, 4))
# print(divi(8, 4))