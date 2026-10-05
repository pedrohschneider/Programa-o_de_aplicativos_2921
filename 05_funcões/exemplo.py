# O que é uma função?

# Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ele permite organizar e reutilizar código.

# 1.0 Criando uma função
# utilizar a palavra def para uma função


def saudacao():
    print("Olá, seja bem vindo")


# para executar a função, chamamos seu nome:
saudacao()


# 2. Função com parâmetro
def saudacao_nome(nome):
    print(f"Olá, {nome}")


saudacao_nome("Raimundo")
saudacao_nome("Sergino")


# 3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")


apresentar("Maria", 17)


# 4. Função com cálculo
def somar_com_print(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")


somar_com_print(10, 5)

# 5. Retornando um valor
# O return devolve um valor para o local onde a função foi chamada


def somar(numero1, numero2):
    return numero1 + numero2


resultado = somar(10, 5)
print(resultado)


# 6. Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


resultado = verificarIdade(20)
print(resultado)


# 7. Parâmetro com valor padrão
# podemos definir um valor padrão para um parâmetro
def saudacao_padrao(nome="Aluno"):
    print(f"Olá , {nome}")


saudacao_padrao()
saudacao_padrao("João")


# 8. Vários parâmetros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


print(calcularMedia(8, 9, 7))


# 9. Funções para organizar um programa
def cadastrarProduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    return nome, preco


def exibirProduto(nome, preco):
    print("\n===== Produto =====")
    print(f"nome: {nome}")
    print(f"Preço: R${preco}")


nome, preco = cadastrarProduto()
exibirProduto(nome, preco)