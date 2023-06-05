#NESSE MODELO, EH IMPOSSIVEL VENCER O COMPUTADOR
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    opcao = int(input("1 - para jogar apenas uma partida\n2 - para jogar um campeonato\n"))
    if opcao == 1:
        print("\nVocê escolheu jogar apenas uma partida!")
        partida()
    elif opcao == 2:
        print("\nVocê escolheu jogar no modo campeonato!")
        campeonato()

def computador_escolhe_jogada(a,b):
    controle = 1
    controle2 = b
    mult_m1 = []
    possivel_escolher = False
    while controle <= 15:
        mult_m1.append((b + 1) * controle)
        controle = controle + 1
    while controle2 > 0 and possivel_escolher == False:
        for x in mult_m1:
            if a - controle2 == x:
                possivel_escolher = True
        controle2 = controle2 - 1
    if possivel_escolher == True:
        return controle2 + 1
    elif a - b < 0:
        return a
    else:
        return b

def usuario_escolhe_jogada (c,d):
    pecas_jogador = int(input("Quantas peças você quer tirar? "))
    while pecas_jogador > d or pecas_jogador > c or pecas_jogador < 1:
        pecas_jogador = int(input("Jogada inválida. Tente de novo.\n\nQuantas peças você quer tirar? "))
    return pecas_jogador

def partida():
    n = int(input("Quantas peças no jogo? "))
    m = int(input("Limite de peças por jogada? "))
    controle = 1
    mult_m1 = []
    while controle <= 15:
        mult_m1.append((m + 1) *controle)
        controle = controle + 1
    usu_comeca = False
    for x in mult_m1:
        if n == x:
            usu_comeca = True
    if usu_comeca:
        print("\nVocê começa!\n")
        while n > 0:
            jog_usu = usuario_escolhe_jogada(n, m)
            n = n - jog_usu
            print("Você tirou", jog_usu, "peças.")
            if n != 0:
                if n == 1:
                    restar = "Resta apenas uma peça"
                else:
                    restar = "Restam"
                    fim = "peças"
                print(restar, n, fim, "no tabuleiro.")
            else:
                print("Fim de jogo! Você ganhou!")
                return [0, 1]
            jog_pc = computador_escolhe_jogada(n, m)
            n = n - jog_pc
            if jog_pc == 1:
                fim = "peça."
            else:
                fim = "peças."
            print("O computador tirou", jog_pc, fim)
            if n != 0:
                print("Restam", n, "peças no tabuleiro.")
            else:
                print("Fim de jogo! O computador ganhou!")
                return [1, 0]
    else:
        print("\nComputador começa!\n")
        while n > 0:
            jog_pc = computador_escolhe_jogada(n, m)
            n = n - jog_pc
            if jog_pc == 1:
                fim = "peça."
            else:
                fim = "peças."
            print("O computador tirou", jog_pc, fim)
            if n != 0:
                if n == 1:
                    restar = "Resta apenas uma peça"
                else:
                    restar = "Restam"
                    fim = "peças"
                print(restar, n, fim, "no tabuleiro.")
            else:
                print("Fim de jogo! O computador ganhou!")
                return [1, 0]
            jog_usu = usuario_escolhe_jogada(n, m)
            n = n - jog_usu
            print("Você tirou", jog_usu, "peças.")
            if n != 0:
                print("Restam", n, "peças no tabuleiro.")
            else:
                print("Fim de jogo! Você ganhou!")
                return [0, 1]
def campeonato():
    n_partidas = 1
    placar_pc = 0
    placar_usu = 0
    while n_partidas <= 5:
        print("\n*** RODADA", n_partidas, "***\n")
        placar = partida()
        placar_pc = placar_pc + placar[0]
        placar_usu = placar_usu + placar[1]
        n_partidas = n_partidas + 1
    print("Placar: Você", placar_usu, "X", placar_pc, "Computador")

main()
