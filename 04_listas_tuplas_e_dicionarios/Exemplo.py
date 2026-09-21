#Listas, Tuplas e Dicionarios

#1. Listas

#  Listas são utilizadas para armazenar vários valores
#  dentro de uma unica váriavel.

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

#2. Acessando elementos da lista

print(nomes[0])

print(nomes[1])

#Podemos acessar o ultimo elemento usando -1

print(nomes[-1])

#3. Alterando elementos

# As listas são mutáveis, ou seja, os elementos podem ser alterados

nomes[0] = "Pedro"
print(nomes)

#4. Adicionando elementos

#append() adiciona um elemento novo no final da lista.

nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma determinada posição.

nomes.insert(1, "Mariana")
print(nomes)



