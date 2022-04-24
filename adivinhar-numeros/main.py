import random

def numero_aleatorio (inicio:int, fim:int):
    '''
        Coloque apenas o numero máxima do intervalo 
    '''
    numero = random.randint(inicio,fim)

    return numero

print("Defina um intervalo de números !")

inicio = int(input("Começo: "))
fim = int(input("Fim: "))
numero_secreto = numero_aleatorio(inicio, fim)

acertou = False
contador_de_estimativas = 0

while acertou == False:
    contador_de_estimativas += 1
    
    print("Tente acertar o número secreto...")
    estimvativa = int(input("R: "))

    if(estimvativa > numero_secreto):
        print("Tente novamente! Você adivinhou muito alto")
    
    elif (estimvativa < numero_secreto):
        print("Tente novamente! Você adivinhou muito baixo")
        
    else:
        print("Parabéns, Você acertou !!!")
        print("Numero de estivamativas: {estimativas}".format(estimativas = contador_de_estimativas))
        acertou = True