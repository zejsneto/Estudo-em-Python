from math import * 

#Ex1
'''
Vamos escrever um código que calcula o fatorial de um número. O fatorial é
calculado somente para os números naturais, ou seja, números inteiros e
positivos. Dado um número natural n, seu fatorial é o produto de todos os
seus antecessores até 1, representamos o fatorial de um número como n!
'''
numero=int(input("Digite um numero: "))
fatorial = 1
for x in range(numero,1,-1):
    fatorial=fatorial*x
print("O resultado final é",fatorial)

#Ex2
#Imprima a sequência de Fibonacci usando for.
# 1 2 3 4 5 6 7  8  9  10 11 12
# 1 1 2 3 5 8 13 21 34 55 89 144
n = int(input("Que termo da sequência de Fibonacci você deseja encontrar: "))
ultimo=1
penultimo=1

if (n==1):
    print("O %dº termo é: %d" %(n,penultimo))
elif (n==2):
    print("O %dº termo é: %d" %(n,ultimo))
else:
    atual = 0
    for i in range(2,n): #2<=i<n
        atual = ultimo + penultimo                #2 
        penultimo = ultimo                        #1
        ultimo = atual                            #2
    print("O %dº termo é: %d" %(n,atual))

#Imprima a sequência de Fibonacci usando while.
# 1 2 3 4 5 6 7  8  9  10 11 12
# 1 1 2 3 5 8 13 21 34 55 89 144
n = int(input("Até qual termo da sequência de Fibonacci você deseja imprimir: "))
penultimo = 1
ultimo = 0
contador = 0
sequencia = 0

while (contador<=n-1):
    sequencia = ultimo + penultimo
    penultimo = ultimo
    ultimo = sequencia
    contador = contador + 1
    print("O %dº termo é: %d" %(contador,sequencia))

#Ex3
'''
Crie uma Lista de números inteiros de tamanho 5. Preencha
essa Lista com entradas fornecidas pelo usuário. Exiba como
saída o conteúdo do índice 3 dessa Lista.
(Usar estrutura de repetição)
'''
L=[]
while (len(L)<5):
    n=int(input("Digite um valor: "))
    L.append(n)
print("O valor do terceiro índice é: ",L[2])

#Ou

L=[]
while True:
    n=int(input("Digite um valor: "))
    L.append(n)
    if (len(L)==5):
        print("O valor do terceiro índice é: ",L[2])
        break

#Ex4
'''
Faça um programa que armazene 10 números inteiros
informados pelo usuário em uma Lista. Exiba como saída o
MAIOR numero dessa Lista.
OBRIGATÓRIO O USO DE LAÇO DE REPETIÇÃO PARA LEITURA DA LISTA.
'''
L=[]
contador = 0
print("Digite valores diferentes")
while (len(L)<10):
    contador = contador + 1
    n=int(input("Digite o %dº valor: " %contador))
    L.append(n)

L1=L[:]
L.sort(reverse = True)
for i in range(0,len(L1)):
    if L1[i]==L[0]:
        indice=i

print("O maior valor da lista é %d e ele é o índice %d."%(L[0],indice))


#Ex5
'''
Faça um programa que receba uma frase e diga quantas vezes
uma palavra especifica foi digitada.
'''
frase = input("Digite uma frase: ")
quantia = len(frase.split())
print("A frase tem %d palavras" %(quantia))

#DO PROFESSOR
a=str(input("Digite uma frase: "))
count = 1
if (a[0]==" "):
    count=0
for i in range(0,len(a)):
    if a[i]==" " and a[i+1]!=" ":
        count = count + 1
print("A frase tem %d palavras"%count) 

#Ou

frase = input("Informe uma frase: ")
palavra = input("Informe o palavra que deseja contar: ")
contador=str(frase.count(palavra))
print("Na frase: '{0}' , a palavra {1} foi escrita {2} vezes" .format(frase,palavra,contador))