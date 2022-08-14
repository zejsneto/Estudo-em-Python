from math import * 

#Ex1
'''
● Faça um programa que lê um ano como entrada e verifica se esse ano é bissexto.
● Regras para definição de ano bissexto:
o Se o ano for divisível por 400 ele é bissexto! Acaba aqui!
o Se o ano não for divisível por 400, para ser bissexto ele deve:
• Ser divísivel por 4
• Não ser divisível por 100
● Faça o programa com somente 1 if, 1 else, nenhum elif
● Alguns anos bissextos para verificação: 1904, 1920, 1932, 2016

'''
ano = int(input("Digite o ano: "))
if (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
    print("%d é um ano bissexto" % ano)
else:
    print("%d não é um ano bissexto" % ano)

#Ex2
'''
Você foi designado para ajudar um departamento da empresa Xis&Zi a encontrar os
ângulos internos dos triângulos que correspondem a alguns tipos de peças. Por meio das
medidas encontradas, você deverá apontar o tipo do triângulo. Desenvolver um programa
em Python que de acordo com os ângulos informados para o usuário, mostre qual tipo do
triângulo
'''
a = int(input("Digite o valor do angulo a: "))
b = int(input("Digite o valor do angulo b: "))
c = int(input("Digite o valor do angulo c: "))

if (a==b) and (b==c) and (a==c):
    print("O triângulo é equilátero")

elif (a!=b )and (b!=c) and (a!=c):
    print("O triângulo é escaleno")

else:
    print("O triângulo é isósceles")

#Ex3
'''
Calcular o preço de uma conta de telefone que é formada por preços
diferenciados: acima a 400 min, R$ 0,15 por min; abaixo ou igual 400 min,
R$ 0,18 por min; e abaixo de 200 min, R$ 0,20 por min.
'''
minutos = float(input("Digite a quantidade de minutos falados: "))

if(minutos>400):
    conta = minutos * 0.15
    print("Sua conta deu %.2f reais." %conta)

if(minutos<=400) and (minutos>=200):   
    conta = minutos * 0.18
    print("Sua conta deu %.2f reais." %conta)

if(minutos<200):   
    conta = minutos * 0.2
    print("Sua conta deu %.2f reais." %conta)