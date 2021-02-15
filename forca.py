def jogar():
    imprime_bem_vindo()

    palavra_secreta = define_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0  # 7
    tentativas_restantes = 6
    rodada = 1
    contador_de_tentativas(tentativas_restantes)

    while not enforcou and not acertou:

        print()
        print("-> Rodada {}".format(rodada))

        contador_de_tentativas(tentativas_restantes)

        rodada += 1
        character(letras_acertadas, erros)

        chute = pede_chute()

        if chute == palavra_secreta:
            imprime_ganhou()
            break

        elif chute in letras_acertadas:

            imprime_letra_ja_foi_usada()

            erros += 1
            tentativas_restantes -= 1
            contador_de_tentativas(tentativas_restantes)

            margem()

        elif chute in palavra_secreta:

            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
            margem()

        else:
            erros += 1
            tentativas_restantes -= 1

            imprime_letra_nao_existe()

            margem()

        enforcou = erros == 6
        if enforcou:

            imprime_enforcado()
            character(letras_acertadas, erros)

            imprime_tentativas_acabaram(palavra_secreta)

        acertou = "_" not in letras_acertadas
        if acertou:
            imprime_ganhou()

    mensagem_fim_do_jogo()


def jogar_novamente():
    print()
    print("Gostaria de jogar novamente?")
    print("(1) - sim")
    print("(2) - não")
    jogar_novamente = int(input())

    if jogar_novamente == 1:
        jogar()


def imprime_bem_vindo():
    print("=====================================================================================")
    print("Bem vindo ao jogo de Forca!")
    margem()

def margem():
    print("-------------------------------------------------------------------------------------")

def imprime_enforcado():
    print()
    print("Você foi enforcado!")


def imprime_ganhou():
    print()
    print("Parabéns! Você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_letra_nao_existe():
    print()
    print("Sua palavra não tem essa letra!")


def imprime_letra_ja_foi_usada():
    print()
    print("Você já adivinhou essa letra! Tente novamente.")


def imprime_tentativas_acabaram(palavra_secreta):
    print()
    print("Suas tentativas acabaram! A Palavra era:", palavra_secreta)


def mensagem_fim_do_jogo():
    print("-------------------------------------------------------------------------------------")
    print("Fim do jogo")
    print("=====================================================================================")


def define_palavra_secreta():
    import random

    arquivo = open("./resources/palavras.txt", "r")
    palavras_secretas = []
    for linha in arquivo:
        linha = linha.strip()
        palavras_secretas.append(linha)
    arquivo.close()

    return palavras_secretas[random.randrange(0, len(palavras_secretas))].upper()


def contador_de_tentativas(tentativas_restantes):
    print()
    if (tentativas_restantes == 6):
        print("Você terá 6 tentativas!")
    else:
        print("Ainda restam {} tentivas".format(tentativas_restantes))

def haste_forca():
    print("|               ")

def character_head(erros):
    if erros >= 1:
        print("|      ---      ")
        print("|     |x x|     ")
        print("|      ___      ")
    else:
        haste_forca()
        haste_forca()
        haste_forca()

def character_torax(erros):
    if erros >= 2 and erros < 3:
        print("|       |       ")
        print("|       |       ")
        print("|       |       ")
        print("|       |       ")
    elif erros >= 3 and erros < 4:
        print("|     __|       ")
        print("|    /  |       ")
        print("|  _/   |       ")
        print("|       |       ")
    elif erros >=4:
        print("|     __|__     ")
        print("|    /  |  \    ")
        print("|  _/   |   \_  ")
        print("|       |       ")
    else:
        haste_forca()
        haste_forca()
        haste_forca()
        haste_forca()

def character_legs(erros):
    if erros >=5 and erros < 6:
        print("|      /        ")
        print("|     /         ")
        print("|   _/          ")
    elif erros >= 6:
        print("|      / \      ")
        print("|     /   \     ")
        print("|   _/     \_   ")
    else:
        haste_forca()
        haste_forca()
        haste_forca()

def character(letras_acertadas, erros):
    print()
    print(" _______        ")
    print("|/      |       ")
    character_head(erros)
    character_torax(erros)
    character_legs(erros)
    print("|               ")
    print("|_", letras_acertadas)

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


if __name__ == "__main__":
    jogar()
    jogar_novamente()
