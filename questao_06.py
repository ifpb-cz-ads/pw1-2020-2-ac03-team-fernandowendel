# QUESTAO 06

# Escreva um programa para aprovar o empréstimo bancário para
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
# superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
# casa a comprar dividido pelo número de meses a pagar.
 
v_casa = float(input("Informe o valor do imovel: R$ "))
salario = float(input("Informe o seu salario: R$ "))
quant_anos = float(input("Informe a quantidade de ANOS para pagar: "))

if v_casa > 0 and salario > 0 and quant_anos > 0:
    quant_mes = quant_anos * 12
    parcela_max = salario * 0.3
    parcela = v_casa / quant_mes

    if parcela > parcela_max:
        print("Parcela R$%.2f maior que 30 da renda: " % parcela)
    else:
        print("Parcela de R$%.2f em %.f meses." % (parcela, quant_mes))
else:
    print("Valor menor ou igual a zero inserido... Erro: Operacao invalida!")