# QUESTAO 02

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    if n3 > n2:
        menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    if n3 > n1:
        menor = n1

if n3 > n1 and n3 > n2:
    maior = n3
    if n1 > n2:
        menor = n2
    if n2 > n1:
        menor = n1

print("Maior: %.d e Menor: %.d" % (maior, menor))    