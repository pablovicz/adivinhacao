print("=====================================================================================")
print("Bem vindo ao jogo de adivinhação!")

import random

max_range = 0
total_de_tentativas = 0
pontos = 1000
bonus = 0
tentativa = 1

print("-------------------------------------------------------------------------------------")
print("Qual nível de dificuldade?")
print("(1) Fácil - Range: 1 - 30 |  10 tentativas")
print("(2) Médio - Range: 1 - 40 |  5 tentativas")
print("(3) Difícil - Range: 1 - 50 |   tentativas")
nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 10
    max_range = 30
    bonus = 100
elif nivel == 2:
    total_de_tentativas = 5
    max_range = 40
    pontos = pontos + 200
    bonus = 300
else:
    total_de_tentativas = 3
    max_range = 50
    pontos = pontos + 400
    bonus = 500

numero_secreto = random.randrange(1, max_range)

for tentativa in range(1, total_de_tentativas + 1):
    ##while (tentativa <= total_de_tentativas):

    print("-------------------------------------------------------------------------------------")
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e {}: ".format(max_range)))

    if (chute < 1 or chute > max_range):
        print("Voce deve digitar um número entre 1 e {}!".format(max_range))
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você Acertou!")
        pontos = pontos + bonus
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    tentativa = tentativa + 1

if not acertou:
    print("-------------------------------------------------------------------------------------")
    print("O número secreto era:", numero_secreto)

print("-------------------------------------------------------------------------------------")
print("Você fez", pontos, "pontos!")
print("Fim do jogo")
print("=====================================================================================")
