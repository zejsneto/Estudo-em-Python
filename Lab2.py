#Estudo em Python
#Lab 1

#Exercício 1 
#Faça um programa para exibir a idade de uma pessoa tendo como entrada a sua faixa etária, de acordo com a tabela abaixo:
#Faixa etária | Idade
#Bebê         | menor que 2 anos
#Criança      | de 3 a 10 anos
#Adolescente  | de 11 a 17 anos
#Adulto       | de 18 a 64 anos
#Idoso        | maior que 65 anos
faixa = input("Digite a faixa etária: ")

if faixa == "Bebê":
    print("menor que 2 anos")
if faixa == "Criança":
    print("de 3 a 10 anos")
if faixa == "Adolescente":
    print("de 11 a 17 anos")
if faixa == "Adulto":
    print("de 18 a 64 anos")
if faixa == "Idoso":
    print("maior que 65 anos")

#Exercício 2
#Uma loja está fazendo uma promoção para clientes que comprem três produtos. Ler o valor de cada produto e calcular o valor total da compra. Caso o total da compra seja acima de R$ 500,00 ele terá 20% de desconto, senão o desconto será de 10%. Calcular e mostrar o desconto para um cliente (considere duas casas decimas na saída).
a = float(input("Digite o valor do primeiro produto: "))
b = float(input("Digite o valor do segundo produto: "))
c = float(input("Digite o valor do terceiro produto: "))
d = a + b + c
if d > 500:
    desconto = d*0.2
else:
    desconto = d*0.1
print("Desconto: %.2f" % desconto)

#Exercício 3
#Escreva um programa que determine o nome de uma forma a partir de seu número de lados. Leia o número de lados do usuário e relate o nome apropriado como parte de uma mensagem significativa. Seu programa deve oferecer suporte a formas de 3 (incluindo) a 10 lados. Se um número de lados fora desse intervalo for inserido, seu programa deverá exibir uma mensagem de erro.
a = int(input(""))
if a == 3:
    print("triângulo")
if a == 4:
    print("quadrado")
if a == 5:
    print("pentágono")
if a == 6:
    print("hexágono")
if a == 7:
    print("heptágono")
if a == 8:
    print("octógono")
if a == 9:
    print("eneágono")
if a == 10:
    print("decágono")
if a > 10:
    print("Erro!")

#Exercício 4
#Uma loja dá desconto de 10% para compras à vista, 5% para compras em 2 ou 3 parcelas e não dá desconto para compras acima de 3 parcelas. Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao outro possível desconto) aos clientes que comprarem um total superior a R$5.000,00. Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor do desconto,  o valor final da compra com desconto e o valor de cada parcela. Utilize duas casas decimais.
a = float(input("Digite o valor da compra: "))
b = int(input("Digite a quantidade de parcelas: "))
if a > 5000:
  desconto1 = a * 0.05
if a < 5000:
  desconto1 = 0
if b == 1:
  desconto2 = a * 0.1
if b == 2:
  desconto2 = a * 0.05
if b == 3:
    desconto2 = a * 0.05
if b > 3:
    desconto2 = 0
c = desconto1 + desconto2
print("Desconto total: %.2f" % c)
d = a - c
print("Valor final da compra com desconto: %.2f" % d)
e = d / b
print("Cada parcela será de: %.2f" % e)

#Exercício 5
#Desenvolva um algoritmo que pergunte ao usuário se ele deseja calcular o volume do Dodecaedro (12 faces) ou do Icosaedro (20 faces) regular. Para realizar o cálculo, receba do usuário o valor da aresta a. Consulte as fórmulas na internet.
from math import sqrt

forma = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
a = float(input("Digite o valor da aresta a em metros: "))

if forma == "dodecaedro":
    volume = ((15+7*sqrt(5))/4) * a**3
else:
    volume = (5/12) * (3+sqrt(5)) * a**3

print("O volume de um %s regular com %.2f de aresta é: %.2f" % (forma, a, volume))

#Exercício 6
#A duração de um mês varia de 28 a 31 dias. Neste exercício, você criará um programa que lê o nome de um mês do usuário como uma string. Em seguida, seu programa deve exibir o número de dias naquele mês. Exiba “28 ou 29 dias” para fevereiro para que os anos bissextos sejam considerados.
a = input("")
if a == "janeiro":
    print("31 dias")
if a == "fevereiro":
    print("28 ou 29 dias")
if a == "março":
    print("31 dias")
if a == "abril":
    print("30 dias")
if a == "maio":
    print("31 dias")
if a == "junho":
    print("30 dias")
if a == "julho":
    print("31 dias")
if a == "agosto":
    print("31 dias")
if a == "setembro":
    print("30 dias")
if a == "outubro":
    print("31 dias")
if a == "novembro":
    print("30 dias")
if a == "dezembro":
    print("31 dias")
  
#Exercício 7
#Uma granja classifica os ovos produzidos em pequeno e grande antes de embalá-los. Faça um programa que receba a medida dos ovos e os classifique seguindo a tabela a seguir:
#Tamanho               |Classificação
#menor que 30 mm       |pequeno
#maior ou igual a 30 mm|grande
a = float(input("Digite a medida do ovo: "))
if a < 30:
    print("pequeno")
if a == 30:
    print("grande")
if a > 30:
    print("grande")
  
#Exercício 8
#Um reservatório vazio deve ser abastecido por uma bomba. Faça um programa em Python para calcular o tempo (em horas, minutos e segundos) necessário para que o reservatório fique completamente cheio; então, exiba a resposta.  A vazão da bomba (em litros por segundo) e a capacidade do reservatório (em litros) devem ser digitadas pelo usuário.
a = float(input("Digite a vazão da bomba em l/s: "))
b = float(input("Digite a capacidade do reservatório: "))
c = b / a
e = c / 3600
f = int("%.0d" % e)
g = float(c - f * 3600)
h = g / 60
i = int("%.0d" % h)
j = f * 3600 
k = i * 60
l = j + k
m = c - l
n = int("%.0d" % m)

print("Tempo necessário para encher o reservatório: %d:%d:%d" % (f,i,n))