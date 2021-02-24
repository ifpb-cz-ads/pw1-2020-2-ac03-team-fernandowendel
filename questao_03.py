'''
3) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
   Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
   Para os inferiores ou iguais, de 15%.

'''

salario = float(input('Informe o salario: '))

if salario < 0:
    print('Salario invalido !')
if salario > 1250 : 
    novo_salario = salario * (1 + 10 / 100) # aumento de 10%
    aumento = novo_salario - salario # valor do aumento
else : 
    novo_salario = salario * (1 + 15 / 100) # aumento de 15%
    aumento = novo_salario - salario # valor do aumento

print(f'O novo salario eh R$ {novo_salario:.2f} e o valor do aumento eh R$ {aumento:.2f}')
