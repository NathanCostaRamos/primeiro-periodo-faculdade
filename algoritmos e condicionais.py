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

#b) Escreva um algoritmo para ler um número inteiro e retornar se ele é maior, igual ou menor que zero. 

num = int(input("Digite um número inteiro:"))

if (num==0):
  print ("nulo")
elif (num > 0):
  print ("positivo")
else:
  print ("negativo")

#c) Faça um algoritmo que leia um número inteiro e retorne se o número é par o ímpar.

numero = int(input("Digite um número inteiro:"))

if (numero % 2 == 0):
  print("Seu número é um numero par.")
else:
  print("Seu número é um numero impar.")

#d) Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 80, menor que 25 ou igual a 40.

Num = int(input("digite um número inteiro"))

if (Num > 80):
  print ("Seu número é maior que 80")
elif (Num < 25):
  print ("Seu número é menor que 25.")
elif (Num == 40):
   print("Seu número é igual a 40.")
else:
  print ("Seu número não está entre os requisitos.")

print("-------------------------------------------------------------------------------------------------------------------------------------------")

#e)Elabore um algoritmo para testar se uma senha digita é igual a “batatafrita”. Se a senha estiver correta escreva “Acesso permitido”, do contrário emita a mensagem “Você não tem acesso ao sistema”.

senha= str(input("informe a senha "))

if (senha=="batatafrita"):
  print("acesso permitido ")
else:
  print("senha incorreta ")

#f) Escrever um algoritmo que leia três valores inteiros distintos e os escreva em ordem crescente.

numero1 = int(input("coloque um número: "))
numero2 = int(input("coloque um número: "))
numero3 = int(input("coloque um número: "))

if (numero1 > numero2 > numero3):
   print("A ordem crescente dos números são: ", numero1, numero2, numero3)
elif (numero1 > numero3 > numero2):
   print("A ordem crescente dos números são: ", numero1, numero3, numero2)
elif (numero2 > numero1 > numero3):
   print("A ordem crescente dos números são: ", numero2, numero1, numero3)
elif (numero2 > numero3 > numero1):
   print("A ordem crescente dos números são: ", numero2, numero3, numero1)
elif (numero3 > numero1 > numero2):
   print("A ordem crescente dos números são: ", numero3, numero1, numero2)
elif (numero3 > numero2 > numero1):
   print("A ordem crescente dos números são: ", numero3, numero2, numero1)
else:
   print("Seus números são iguais.")

#g) Escrever um algoritmo para uma empresa que decide dar um reajuste a seus funcionários de acordo com os seguintes critérios:
#a) 50% para aqueles que ganham menos do que três salários mínimos;
#b) 20% para aqueles que ganham entre três até dez salários mínimos;
#c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
#d) 10% para os demais funcionários.
#Obs: Leia o valor do salário mínimo

salarioMinimo= 1.320
salarioFuncionario= int(input("Digite seu salário atual "))

if (salarioFuncionario < (salarioMinimo*3)):
   SalarioNovo = salarioFuncionario + (salarioFuncionario*0.5)
   reajuste ="50%"
   aumento = SalarioNovo - salarioFuncionario
elif((salarioFuncionario > (salarioMinimo*3)) or (salarioFuncionario <= (salarioMinimo*10))):
   SalarioNovo = salarioFuncionario + (salarioFuncionario*0.2)
   reajuste = "20%"
   aumento = SalarioNovo - salarioFuncionario
elif((salarioFuncionario > (salarioMinimo*3)) or (salarioFuncionario <= (salarioMinimo*10))):
   SalarioNovo = salarioFuncionario + (salarioFuncionario*0.15)
   reajuste = "15%"
   aumento = SalarioNovo - salarioFuncionario
else:
   SalarioNovo = salarioFuncionario + (salarioFuncionario*0.1)
   reajuste = "10%"
   aumento = SalarioNovo - salarioFuncionario
   
print("Seu salário levou um reajuste de ", reajuste,", ficando atualmente em ", SalarioNovo, ",levando um aumento de", aumento,  )

#h) Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor do produto e imprima o valor de venda para o produto.

compraProduto = int(input("preço do produto:"))

if compraProduto > 20:
   valorProduto = compraProduto + (compraProduto*0.45)
   lucro = compraProduto - valorProduto
else:
   valorProduto = compraProduto + (compraProduto*0.3)
   lucro = compraProduto - valorProduto

print("O valor do produto aumentou para R$", valorProduto, "obtendo o lucro de R$", lucro)
   
#i) A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%.   

precocarro = int(input("valor do carro:  "))
anocarro = int(input("Ano do carro: "))

if anocarro > 2000:
   valorcarro = precocarro - (precocarro*0.07)
   desconto = "7%"
else:
   valorcarro = precocarro - (precocarro*0.12)
   desconto = "12%"
   
print("o carro vale: ", precocarro, "com o desconto de ", desconto, ", reduziu para ",valorcarro)

#j) Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

nume = int(input("Digite um numero inteiro:"))

if ((nume >= 100) or (nume <= 200)):
   print("Seu número está dentro do intervalo aceito")
else:
   print("Seu número não está dentro do intervalo aceito")