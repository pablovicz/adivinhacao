print("=====================================================================================")
print("Bem vindo!")
print("-------------------------------------------------------------------------------------")

import forca
import adivinhacao

print("Escolha o seu jogo: ")
print("(1) Forca")
print("(2) Adivinhação")
jogo_escolhido = int(input("Qual Jogo?"))

if jogo_escolhido == 1:
    print()
    forca.jogar()
    forca.jogar_novamente()
elif jogo_escolhido == 2:
    print()
    adivinhacao.jogar()
