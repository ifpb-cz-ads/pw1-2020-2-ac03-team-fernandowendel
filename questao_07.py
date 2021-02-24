'''
7) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias 
e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

'''

consumo = float(input('Informe a quantidade de KWh: '))
tipo_instalacao = input('Qual o tipo da instalacao: ')

if consumo < 0 :
    print('Desculpe, valor de consumo invalido !')

elif tipo_instalacao == 'R' :

    if consumo <= 500 :
        preco = consumo * 0.40
    else: 
        preco = consumo * 0.65

    print(f'O preco a se pagar eh R$ {preco:.2f}')

elif tipo_instalacao == 'C' :

    if consumo <= 1000 :
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60

    print(f'O preco a se pagar eh R$ {preco:.2f}')

elif tipo_instalacao == 'I' : 

    if consumo <= 5000 : 
        preco = consumo * 0.55
    else: 
        preco = consumo * 0.60

    print(f'O preco a se pagar eh R$ {preco:.2f}')

else:
    print('Tipo de residencia invalida !')


