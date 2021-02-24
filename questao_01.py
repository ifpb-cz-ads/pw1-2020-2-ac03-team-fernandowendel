
# Deus eu e amo demais ! me perdoa por tudo !

'''
1) Escreva um programa que pergunte a velocidade do carro de um usuário. 
   Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
   Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

'''


velocidade = float(input('Informe a velocidade do carro em Km/h: '))


if velocidade < 0:
    print('Velocidade invalida ! :(')
elif velocidade > 80 : # or multa > 0
    multa = (velocidade - 80) * 5 
    print(f'voce excedeu o limite de velocidade em {velocidade - 80} Km/h, portanto sera multado em R$ {multa:.2f}')
else :
    print('Voce respeitou o limite de velocidade, portanto não sera multado !')