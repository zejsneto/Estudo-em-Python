#Estudo em Python
#Lab 4

#Exercício 1
#Faça um programa que leia uma quantidade de números que será digitada pelo usuário. Em seguida, digite todos os números, conforme quantidade digitada, e informe o maior deles.

a = int(input("Digite a quantidade de números que serão digitados: "))
i = 2
maior1 = float(input("Digite o 1ºnúmero: "))
while i<=a:
  maior2 = float(input("Digite o %dºnúmero: " %i))
  if maior2>maior1:
    maior1=maior2
  i+=1
   
print("O maior valor é", maior1)

#Exercício 2
#Escreva um programa que exiba uma tabela de conversão de temperatura de graus Celsius para graus Fahrenheit. A tabela deve incluir linhas para todas as temperaturas (de 5 em 5 graus Celsius ) entre um valor inteiro mínimo e um valor inteiro máximo (incluso) digitados pelo usuário. Inclua cabeçalhos apropriados em suas colunas. A fórmula para conversão entre graus Celsius e graus Fahrenheit pode ser encontrada na internet.

a = float(input("Digite o mínimo valor em graus C: "))
b = float(input("Digite o máximo valor em graus C: "))

print("Valor em graus C:   Valor em graus F:")
while a<=b:
  print(a,  (9*a/5)+32)
  a+=5

#Exercício 3
#Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir: 
#E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/N

N = int(input("Digite o valor de N: "))
i=1
E1 = 1
while i<=N:
    E2 = 1/i
    E1 = E1+E2
    i+=1

print(E1)

#Exercício 4:
#Faça um programa que receba um número inteiro maior que 1 e verifique se o número fornecido é primo ou não. Mostre uma mensagem de número primo ou de número não primo. Um número é primo quando é divisível apenas pelo número um e por ele mesmo.

n = int(input("Digite o número desejado: "))
cont = 0
i = 0
while i <= n or cont < 2:
    i = i + 1
    x = n % i
    if x == 0:
        cont = cont + 1
if cont <= 2:
    print("Número primo")
else:
    print("Número não primo")

#Exercício 5
#Faça um programa em Python que leia dois números inteiros positivos do usuário, determina e reporta o maior divisor comum entre eles.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
i=1
valor = 0
if a>b:
    while i<=a:
      i+=1
      if a%i==0 and b%i==0:
        valor=i
      
      
if b>a:
    while i<=b:
      i+=1
      if a%i==0 and b%i==0:
        valor=i
       

print("O maior divisor é",valor)