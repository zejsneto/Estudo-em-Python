from math import * 

#Ex1
'''
A fórmula para calcular a área de uma circunferência é: area = π * raio2
. Considerando que π =
3.14159, efetue o cálculo da área para o valor de raio obtido do usuário. Exiba o resultado.
'''
raio = int(input("Digite o tamanho do raio: "))
pi = 3.14159
area = pi * raio * raio
print("A área do círculo é %.2f " %area)
print("A área do círculo é {0:.2f} " .format(area))

#Ex2
'''
Faça um programa que calcule e mostre a área de um triângulo, sendo que a base e a altura são
entradas realizadas pelo usuário. Sabe-se que: Área = (base * altura) / 2. 
'''
base = int(input("Digite o tamanho da base: "))
altura = int(input("Digite o tamanho da altura: "))
areaTri = (base*altura)/2
print("A área do círculo é: ",areaTri)

#Ex3
'''
Faça um programa que recebe o salário de um funcionário, calcula e exibe na tela o salário com
aumento de 25%. 
'''
salario = float(input("Digite o salario: "))
salario125 = salario * 1.25
print("O salário com aumento de 25% é: ",salario125)

#Ex4
'''
Faça um Programa que peça a temperatura em graus Fahrenheit (F) para o usuário. Então,
transforma e exibe a temperatura em graus Celsius (C).
C = (5 * (F-32) / 9)
'''
tempFah = float(input("Digite a temperatura em Fahrenheit: "))
tempC = (5* (tempFah - 32)/9)
print("A temperatura em graus Celsius é: {0:.2f} " .format(tempC))