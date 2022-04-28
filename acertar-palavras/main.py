from pickle import TRUE
import random

livros_da_biblia = ['Gênesis', 'Êxodo','Números','Deuteronômio','Josué','Juízes','Rute','1Samuel','2Samuel','1Reis','2Reis']
livro_escolhido = random.choice(livros_da_biblia)
letras = list(livro_escolhido)

print("Qual é o seu nome ? ")
nome_usuario = input("R:")

print("Boa sorte, {nome} !".format(nome = nome_usuario))

acertos = []
tentativas = 12

# Cria uma lista de acertos baseada na lista
for x in range(len(letras)):
    acertos += [False]

while tentativas != 0:
    numero_acertos = len(letras)

    if numero_acertos == 0:
        print("Parabéns!!")
        break

    chute = input("R: ")


    for posicao in range(len(letras)):
        if chute == letras[posicao]:
            numero_acertos -= 1
            acertos[posicao] = [True]

        if acertos[posicao] == [True]:
            print(letras[posicao])
        else:
            print("__")
    tentativas -= 1
        