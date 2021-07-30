# a = int(input('Digite Número: '))
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))

# a = int(input('Digite Número: '))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#             print(num)

# nota = int(input('Entre com nota: '))
# while nota > 10:
#     nota = int(input('Entre com a nota correta: '))
# print(nota)

a = int(input('Entre com o número: '))
div = 0
for x in range(1, a+1):
	resto = a % x
	if resto == 0:
		div += 1

if div == 2 :
	print('número {} é primo'.format(a))
else:
	print('número {} não é primo'.format(a))
