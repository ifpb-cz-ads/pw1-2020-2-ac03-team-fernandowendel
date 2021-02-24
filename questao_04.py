# QUESTAO 04

viagem = float(input("Informe a distacia que quer percorre km: "))

if viagem > 0: 
    if viagem <= 200 and viagem > 0:
        calc_viagem = viagem * 0.5
    else:
        calc_viagem = viagem * 0.45
    print("Valor cobrado = R$%.2f" % calc_viagem)
else:
    print("Valor invalido!")