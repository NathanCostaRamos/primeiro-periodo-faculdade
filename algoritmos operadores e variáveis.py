# a)Crie uma variável de atribua a ela o valor de uma hora inteira. O algoritmo deve processar aconversão dessa hora em minutos e segundos e imprimir na tela essas conversões. 
hora = int(input("que horas são?"))
minutos = hora*60
segundos = minutos*60
print("um total de", hora, "será", minutos, "e será", segundos)

#b) Crie uma variável que receba um valor que é pago por um produto, um segundo valor que é o preço do produto e retorne em outra variável o troco a ser dado. Considere que o valor pago será igual ou maior que o valor do produto.
valorp = 1000
valorpro = 500
troco=(valorpro - valorp)

print("o troco é de:",troco)

#c) Crie duas variáveis que guarde dois números inteiros, e imprimar o quociente e o resto da divisão inteira entre eles. 
num1= int(input("escreva um número inteiro"))
num2= int(input("digite outro número inteiro"))
quociente = num1/ num2
print("seu quociente será de", quociente)

#d)Uma variável que guarde o salário fixo de um vendedor, outra o total ($) de vendas por ele efetuadas e outra o percentual de comissão que ele ganha sobre o total vendido. O algoritmo deve imprimir a comissão do vendedor e o seu salário final.

salario_fixo = float(input("Informe o salário fixo do vendedor: "))
total_vendas = float(input("Informe o total de vendas efetuadas: "))
percentual_comissao = float(input("Informe o percentual de comissão (em decimal): "))


comissao = total_vendas * percentual_comissao


salario_final = salario_fixo + comissao


print("Comissão do vendedor: $", comissao)
print("Salário final do vendedor: $", salario_final)

# e)Crie 3 variáveis para guardar três notas informadas por um aluno e exiba a sua média aritmética.

jorginho= 10
junin= 4
jotinha= 6
mediaaritmetica= (junin + jorginho + jotinha )//3

print("a média entre, junin, jorginho, jotinha é:", mediaaritmetica)

#f)Um motorista deseja colocar no seu tanque X reais de gasolina. Crie uma variável que guarde o preço do litro da gasolina e o valor que o motorista possui para colocar a gasolina. Imprima quantos litros de gasolina o motorista conseguiu colocar no tanque. 

preco_litro = float(input("Informe o preço do litro da gasolina: "))
valor_disponivel = float(input("Informe o valor disponível para colocar gasolina: "))

litros_gasolina = valor_disponivel / preco_litro

print("Quantidade de litros de gasolina: ", litros_gasolina)
