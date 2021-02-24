'''
5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
 Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/).
  Exiba o resultado da operação solicitada.

'''

num_01 = int(input('Informe o primeiro numero: '))
num_02 = int(input('Informe o segundo numero: '))
operador = input('Qual operacao deseja realizar, "+", "-", "/" ou "*" ?  ')

if operador == '+' : 
    print('%d + %d = %d' %(num_01, num_02, (num_01 + num_02)))
elif operador == '-' : 
    print('%d - %d = %d' %(num_01, num_02, (num_01 - num_02)))
elif operador == '*' : 
    print('%d * %d = %d' %(num_01, num_02, (num_01 * num_02)))
elif operador == '/' : 
    print('%d / %d = %d' %(num_01, num_02, (num_01 / num_02)))
else : 
    print('Operador invalido :(')