def main():
    print("Bem-vindo ao jogo do NIM!")
    while True:
        try:

            opcao = int(input("\nEscolha:\n1 - Para jogar apenas uma partida\n2 - Para jogar um campeonato de 5 partidas\n"))
            if opcao == 1 or opcao == 2:
                break
        except:
            print("\nEscolha inválida.")

    if opcao == 1:
        print("\nVocê escolheu jogar apenas uma partida!")
        partida()
    elif opcao == 2:
        print("\nVocê escolheu jogar no modo campeonato!")
        campeonato()


def computador_escolhe_jogada(a, b):
    controle = 1
    controle2 = b
    mult_m1 = []
    possivel_escolher = False
    while controle <= 15:
        mult_m1.append((b + 1) * controle)
        controle = controle + 1
    while controle2 > 0 and possivel_escolher is False:
        for x in mult_m1:
            if a - controle2 == x:
                possivel_escolher = True
        controle2 = controle2 - 1
    if possivel_escolher:
        return controle2 + 1
    elif a - b < 0:
        return a
    else:
        return b


def usuario_escolhe_jogada(c, d):
    while True:
        try:
            pecas_jogador = int(input("\nQuantas peças você quer tirar? "))
            if not (pecas_jogador > d or pecas_jogador > c or pecas_jogador < 1):
                break
        except:
            print("\nJogada inválida.")
    return pecas_jogador


def partida():
    n = int(input("\nQuantas peças no jogo? "))
    m = int(input("\nLimite de peças por jogada? "))
    controle = 1
    mult_m1 = []
    while controle <= 15:
        mult_m1.append((m + 1) * controle)
        controle = controle + 1
    usu_comeca = False
    for x in mult_m1:
        if n == x:
            usu_comeca = True
    if usu_comeca:
        print("\nVocê começa!")
        while n > 0:
            jog_usu = usuario_escolhe_jogada(n, m)
            n = n - jog_usu
            print("\nVocê tirou", jog_usu, "peças.")
            if n != 0:
                if n == 1:
                    restar = "\nResta apenas uma peça"
                    fim = ""
                else:
                    restar = "Restam"
                    fim = "peças"
                print("\n" + restar, n, fim, "no tabuleiro.")
            else:
                print("\nFim de jogo! Você ganhou!")
                return [0, 1]
            jog_pc = computador_escolhe_jogada(n, m)
            n = n - jog_pc
            if jog_pc == 1:
                fim = "peça."
            else:
                fim = "peças."
            print("\nO computador tirou", jog_pc, fim)
            if n != 0:
                print("\nRestam", n, "peças no tabuleiro.")
            else:
                print("\nFim de jogo! O computador ganhou!")
                return [1, 0]
    else:
        print("\nComputador começa!")
        while n > 0:
            jog_pc = computador_escolhe_jogada(n, m)
            n = n - jog_pc
            if jog_pc == 1:
                fim = "peça."
            else:
                fim = "peças."
            print("\nO computador tirou", jog_pc, fim)
            if n != 0:
                if n == 1:
                    restar = "\nResta apenas uma peça"
                    fim = ""
                else:
                    restar = "Restam"
                    fim = "peças"
                print("\n" + restar, n, fim, "no tabuleiro.")
            else:
                print("\nFim de jogo! O computador ganhou!")
                return [1, 0]
            jog_usu = usuario_escolhe_jogada(n, m)
            n = n - jog_usu
            print("\nVocê tirou", jog_usu, "peças.")
            if n != 0:
                print("\nRestam", n, "peças no tabuleiro.")
            else:
                print("\nFim de jogo! Você ganhou!")
                return [0, 1]


def campeonato():
    n_partidas = 1
    placar_pc = 0
    placar_usu = 0
    while n_partidas <= 5:
        print("\n*** RODADA", n_partidas, "***")
        placar = partida()
        placar_pc = placar_pc + placar[0]
        placar_usu = placar_usu + placar[1]
        n_partidas = n_partidas + 1
        print("\nPlacar: Você", placar_usu, "X", placar_pc, "Computador")


main()
