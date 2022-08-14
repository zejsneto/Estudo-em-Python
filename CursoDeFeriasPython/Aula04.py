from math import * 

#Ex1
'''
Faça um programa que continue recebendo o valor de um produto pelo usuário até que o mesmo queira encerrar o programa, 
imprimindo assim a soma dos valores inseridos, caso o total seja maior que 1000, dê 10% de desconto.
'''
valorFinal = 0 
while True:
    valorEntrada = float(input("Digite o valor do produto comprado ou 0 para sair: "))
    if (valorEntrada<0):
        print("O valor inserido é inválido, digite novamente")
        valorEntrada = float(input("Digite o valor do produto comprado ou 0 para sair: "))
        if (valorEntrada == 0):
            valorFinal = valorFinal + valorEntrada
            break
    elif (valorEntrada>0):
        valorFinal = valorFinal + valorEntrada
    elif (valorEntrada==0):
        valorFinal = valorFinal + valorEntrada
        break
if valorFinal>1000:
    valorFinal = valorFinal * 0.9
    print("O valor final é (10% desconto): ",valorFinal)
else:
    print("O valor final é: ",valorFinal)
    
#Ex2
'''
Calcular a somatória dos números de 0 a 99
'''
somatoria = 0
for x in range (0,100):
    somatoria = somatoria + x
print(somatoria)

#Ex 3
'''
 Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por
ele mesmo e por 1.
'''
numero = int(input("Digite um número: "))
for i in range(2,numero): # 2<=i<numero
    if(numero==2):
        print("O número %d é primo" %numero)
        break
    resto=numero%i
    if (resto == 0):
        print("O número %d não é primo" %numero)
        break
else:
    print("O número %d é primo" %numero)
       
#Ex4
'''
O Máximo Divisor Comum (MDC) de dois números inteiros positivos, n e m, é o maior
número, d, que divide de forma inteira n e m. Existem vários algoritmosque podem ser
usados para resolver esse problema, incluindo:
● Inicialize d para ser o menor número entre m e n.
● Enquanto d não dividir m e n de forma inteira faça
● Diminua o valor de d em 1
● Relate d como o maior divisor comum de n e m.
Escreva um programa que leia dois números inteiros positivos do usuário e use esse
algoritmo para determinar e reportar seu maior divisor comum.

'''
n = int(input("Digite o valor do primeiro número: "))
m = int(input("Digite o valor do segundo número: "))
d = min(n,m)#função para pegar o menor dos dois valores
for i in range (d,0,-1):
    if (n%i==0)and(m%i==0):#compara os restos até chegar no maximo possivel para os dois (pois esta descendo -1)
        break
print("O Máximo Divisor Comum entre %d e %d é %d"%(n,m,i))