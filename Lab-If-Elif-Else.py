#Estudo em Python
#Lab 3

#Exercício 1
#Neste exercício, você criará um programa que lê uma letra do alfabeto. Se o usuário digitar a, e, i, o ou u, seu programa deverá exibir uma mensagem indicando que a letra inserida é uma vogal. Se o usuário digitar y, seu programa deve exibir uma mensagem indicando que às vezes y é uma vogal (depende da língua, no inglês, por exemplo), e às vezes y é uma consoante. Caso contrário, seu programa deve exibir uma mensagem indicando que a letra é uma consoante.

letra = input("Digite a letra desejada: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print("Essa letra é uma vogal")
elif letra == "y":
  print("Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.")
else:
  print("Essa letra é uma consoante.")

#Exercício 2
#O ano é dividido em quatro estações: primavera, verão, outono e inverno. As datas exatas em que as estações mudam podem variar um pouco de ano para ano por causa da maneira que o calendário é construído. Neste exercício, usaremos as seguintes datas limites:
#Estação    |	Primeiro Dia
#Outono     |   20 de Março                        
#Inverno    |	21 de Junho
#Primavera  |	22 de Setembro
#Verão      |	21 de Dezembro
#Crie um programa que recebe do usuário um mês e um dia. O usuário entrará o nome do mês como uma string, seguido do dia do mês como um inteiro. Então, seu programa deve exibir a estação associada à data que foi introduzida.

dia = int(input("Digite o dia desejado: "))
mes = str(input("Digite o mês desejado: "))

if (mes == "março" and dia >= 20) or mes == "abril" or mes == "maio" or (mes == "junho" and dia < 21):
    print("Outono")
elif (mes == "junho" and dia >= 21) or mes == "julho" or mes == "agosto" or (mes == "setembro" and dia < 22):
    print("Inverno")
elif (mes == "setembro" and dia >= 22) or mes == "outubro" or mes == "novembro" or (mes == "dezembro" and dia < 21):
    print("Primavera")
else:
    print("Verão")

#Exercício 3
#Em uma universidade particular, as notas são mapeadas para pontos da seguinte maneira:
#Nota     Pontos               
#A+	    | 5.0
#A      |   	5.0
#A-	    |4.5
#B+	    |4.0
#B	    |3.5
#B-	    |3.0
#Nota        Pontos               
#C+	    |2.5
#C	    |2.0
#C-	    |1.5
#D+	    |1.0
#D	    |0.5
#F	    |0.0
#Escreva um programa que comece lendo uma nota (em letra) do usuário. Então, o seu programa deve computar e exibir o número equivalente de pontos. Certifique-se de que seu programa gere uma mensagem de erro apropriada se o usuário inserir uma nota inválida.

a = input("Digite a nota em letra, e o sinal +/-: ")
if a == "A+":
    print("A+ é equivalente a 5.0")
elif a == "A":
    print("A é equivalente a 5.0")
elif a == "A-":
    print("A- é equivalente a 4.5")
elif a == "B+":
    print("B+ é equivalente a 4.0")
elif a == "B":
    print("B é equivalente a 3.5")
elif a == "B-":
    print("B- é equivalente a 3.0")
elif a == "C+":
    print("C+ é equivalente a 2.5")
elif a == "C":
    print("C é equivalente a 2.0")
elif a == "C-":
    print("C- é equivalente a 1.5")
elif a == "D+":
    print("D+ é equivalente a 1.0")
elif a == "D":
    print("D é equivalente a 0.5")
elif a == "F":
    print("F é equivalente a 0.0")
else:
    print("Nota inválida")
