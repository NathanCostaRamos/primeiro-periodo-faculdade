#1) Crie uma lista vazia . Imprima a lista.
lista=[]
print(lista)
#2) Crie uma lista “idade” com a idade de 10 pessoas. Imprima a lista.
idade=[19,21,31,45,46,56,43,35,10,13]
print(idade)
#3) Solicite ao usuário uma nova idade e insira na lista. Imprima a lista.
idade1=[19,21,31,45,46,56,43,35,10,13]
idadeAd= int(input("qual sua idade: "))
if idadeAd not in idade1:
  idade1.append(idadeAd)
  print(idade1)
#4) Crie uma nova lista “nome” com o nome de 6 pessoas.Imprima a lista.
listaN = ["maria","Nathan","abner","pedro","luiz","victor"]
print(listaN)
#5) Crie uma nova lista “nome_idade” com o conteúdo das duas listas anteriores. Imprima a lista.
nome_idade=["maria","Nathan","abner","pedro","luiz","victor",19,21,31,45,46,56,43,35,10,13]
print(nome_idade)
#6) Imprima a lista “idade” e imprima o 5º elemento dessa lista.
print(idade)
print(idade[4])
#7) Imprima a lista “idade” e imprima o elemento que está na posição/ índice 5 dessa lista.
print(idade)
print (idade[5])
#8) Imprima a lista “idade” e imprima o elemento que está na posição/indice -5 dessa lista.
print(idade)
print (idade[-5])
#9) Imprima a lista “nome_idade “ e imprima a 4º idade dessa lista
print(nome_idade)
print(nome_idade[9])
#10) Imprima a lista “nome” e informe quantos elementos essa lista possui.
print(listaN)
print(listaN.count)
#11) Concatene a lista “nome” com a lista “idade”
nomeidade = listaN + idade
print(nomeidade)
#12) Crie duas cópias da lista idade e imprima o resultado.
print(idade*2)
#13) Imprima a lista “nome” e verifique se o nome Joana consta ou não nessa lista.
print(listaN) 
"joana" in listaN

#14) Imprima a lista idade e retorne a maior idade, a menor idade e a soma de todas as idades dessa lista.
print(min(idade))
print(max(idade))
print(sum(idade))
#15) Insira na lista “nome” um novo nome e na lista “idade” uma nova idade. Imprima as duas listas.
listaN.append("jeremias")
idade.append("57")
print(listaN)
print(idade)
#16) Insira uma novo nome no início da lista “nome” e uma nova idade no início da lista “idade”. Imprima as listas.
listaN.insert(0, 'jabotão')
idade.insert(0, '67')
print(listaN)
print(idade)
#17) Imprima lista “nome” e a lista “idade e remova a última idade da lista “idade” e o último nome da lista “nome”. Imprima as duas listas.
print(listaN)
print(idade)
listaN.pop()
idade.pop()
print(idade)
Print(listaN)
#18) Imprima a lista “nome” e a lista “idade”. Remova o nome que está na posição/indice 3 da lista “nome” e remova a idade que está na posição 2 da lista idade. Imprima novamente as listas para checagem.
print(listaN)
print(idade)
listaN.pop(3)
idade.pop(1)
#19) Informe um nome e uma idadade existente nas listas “nome” e “idade” e remova esses elementos dessas listas.
print(listaN[3])
print(idade[2])
listaN.pop([3])
idade.pop([2])
print(listaN)
print(idade)
#20) Coloque em ordem crescente as duas listas (nome/idade). Imprima as listas
listaN.sort()
idade.sort()
print(listaN)
print(idade)
#21) Imprima as duas lista (nome/idade) em ordem reversa.
listaN.reverse()
idade.reverse()
print(listaN)
print(idade)
#22) Verifique quantas vezes um determinado número inteiro aparece na lista idade.
idade.count()