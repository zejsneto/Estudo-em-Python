from math import * 

#Ex1
'''
Fazer um programa para imprimir números sequenciais na tela, começando
do número 1 até o número digitado pelo usuário. 
'''
numero = int(input("Digite o numero inicial: "))
i = 1

while (i <= numero):
    print(i)
    i = i + 1
#Ou
num = int(input("Digite o numero inicial: "))
i = 0

while (i <= num):
    print(i)
    i = i + 2

#Ex2
'''
Fazer um programa que imprime todos os números pares de 0 até um
número digitado pelo usuário. 
'''
i = int(input("Digite o numero: "))
num = 0
print(num)
while (num < i):
    num = num + 1
    if (num % 2 == 0):
        print(num)

#ou

i = int(input("Digite o numero: "))
num = 0
while (num <= i):  
    if (num % 2 == 0):
        print(num)
    num = num + 1    

#Ex2
'''
Para o exercício da aula passada, em que era necessário classificar o tipo do
triangulo por meio de seus ângulos, coloque uma estrutura de teste de repetição
no inicio para verificar se a soma dos ângulos é igual a 180. Esse teste pede para
o usuário digitar os valores dos ângulos até que a soma entre eles seja igual a
180.

'''
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
tri = a + b + c

while (tri==180) and (a>0) and (b>0) and (c>0):
    print("O triângulo existe")
    break

else:
    print("O triângulo não existe,digite novamente")

#Ou

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
tri = a + b + c

validador = False
while validador == False:
    if (tri==180) and (a>0) and (b>0) and (c>0):
        if(a>90) or (b>90) or (c>90):
            print("O triângulo existe e é obtusangulo")
        if(a<90) and (b<90) and (c<90):
            print("O triângulo existe e é acutangulo")
        if(a==90) or (b==90) or (c==90):
            print("O triângulo existe e é retangulo")    
        validador == True
        break
    if (tri!=180) or (a<=0) or (b<=0) or (c<=0):
        print("O triângulo não existe, tente novamente")
        validador == False
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        tri = a + b + c

#Ex3
'''
Faça um programa que peça ao usuário digitar uma senha de 4 dígitos.
'''
senha = 1234
senhaDigitada = int(input("Digite a senha (4 digitos): "))
contadorSenha=len(str(senhaDigitada))
validador = False
while validador == False:
    if (senha == senhaDigitada):
        print("A senha está correta!")
        validador=True
        break
    elif (senhaDigitada > 9999) :
        print("Senha inválida, tente novamente com 4 digitos!")
        validador=False
        senhaDigitada = int(input("Digite a senha (4 digitos): "))
    elif (contadorSenha<=3):
        print("Senha inválida, tente novamente com 4 digitos!")
        validador=False
        senhaDigitada = int(input("Digite a senha (4 digitos): "))
    elif (contadorSenha==4) and (senhaDigitada<1000):
        print("A senha está incorreta, tente novamente!")
        validador=False
        senhaDigitada = int(input("Digite a senha (4 digitos): "))
    else:
        print("A senha está incorreta, tente novamente!")
        validador=False
        senhaDigitada = int(input("Digite a senha (4 digitos): "))

#Ex4
'''
Escrever um código que soma a quantidade de horas trabalhadas por um
funcionário nos quinze primeiros dias do mês. A variável dia inicia a execução
valendo 1 (pois representa o primeiro dia do mês) e em seguida o teste (dia
<= 15) é feito. Caso seja verdadeiro, é lido o valor da hora para aquele
determinado dia e a hora total é atualizada somando o novo valor (horaTotal
= horaTotal + hora). Em seguida, o dia é atualizado e a execução volta para o
teste (dia <=15).
'''
dia = 1
horaTotal = 0
while (dia<=15):
    hora = int(input("Digite a quantidade de horas trabalhadas no dia %d: " %dia))
    horaTotal += hora
    dia +=1
print("A quantidade de horas trabalhadas nos primeiros 15 dias foi de %d" %horaTotal)

#Ex5
'''
Programa para calcular as tabuadas do número 1 até o número 10.
'''
tabuada=1

while(tabuada<=10):
    print()
    print("Tabuada do",tabuada)
    j=1
    while(j<=10):
        resultado=tabuada*j
        print("%d X %d = %d"%(tabuada,j,resultado))
        j=j+1
    tabuada=tabuada+1