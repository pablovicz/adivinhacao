print("=====================================================================================")
print("Bem vindo ao jogo de adivinhação!")

import random

numero_secreto = random.randrange(1, 21)
total_de_tentativas = 3
tentativa = 1

for tentativa in range(1, total_de_tentativas + 1):
    ##while (tentativa <= total_de_tentativas):

    print("-------------------------------------------------------------------------------------")
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 20: "))

    if (chute < 1 or chute > 20):
        print("Voce deve digitar um número entre 1 e 20!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você Acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

    tentativa = tentativa + 1

print("-------------------------------------------------------------------------------------")
print("Fim do jogo")
print("=====================================================================================")
