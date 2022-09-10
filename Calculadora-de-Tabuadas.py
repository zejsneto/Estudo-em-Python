#CALCULADORA DE TABUADA EM PYTHON
contador = 0
limite = 10
numero = int(input("Qual tabuada você deseja calcular? \n"))

while (contador <= limite):
  tabuada = numero * contador 
  print('{0} x {1} = {2}'.format(numero,contador,tabuada))
  contador = contador + 1

#PRINT DE TABUADAS EM PYTHON
for x in range(1,11):
  print("Tabuada do ", x)
  for y in range(1,11):
    print(x, "x", y, " = ", x * y)
