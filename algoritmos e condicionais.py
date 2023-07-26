#Elabore uma solução algorítmica em PYTHON para os problemas abaixo presentados:

# a) Escreva um algoritmo que leia dois números e exiba o maior deles.

num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite um numero inteiro:"))

if num1 > num2:
    print("O número ", num1, "é maior que o numero ", num2)
elif num1 == num2:
      print("Os dois números são iguais.")
else:
        print("O número ", num2, "é maior que o número ", num1)
