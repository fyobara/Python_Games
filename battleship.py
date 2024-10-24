import random
import os


def limpar_terminal():
    os.name == 'nt'
    os.system('cls')


def menu_dificuldade():
    print('==================================================')
    print('''Escolha a Dificuldade\n\n(0)Teste\n(1)Fácil\n(2)Médio\n(3)Difícil''')
    print('==================================================')
    opcao = int(input('Insira sua Resposta '))
    print('==================================================\n')
    match opcao:
        case 0:
            return 3
        case 1:
            return 50
        case 2:
            return 42
        case 3:
            return 35
        case _:
            print('==================================================')
            print('!!! Entrada Inválida, Tente Novamente !!!')
            print('==================================================\n')
            menu_dificuldade()


def conferir_vitoria(mapa, jogadas):
    for i in mapa:
        if i not in jogadas:
            return False
    print("Você Venceu!")
    return True


def conferir_derrota(tentativas):
    if tentativas == 0:
        print(f'Você Perdeu')
        return True
    return False


def navios_restantes(mapa, jogadas):
    tamanhos_navios = [1, 1, 2, 2, 3, 4, 5]
    navios = []
    index = 0

    # Agrupar as coordenadas do mapa com base nos tamanhos dos navios
    for tamanho in tamanhos_navios:
        navios.append(mapa[index:index + tamanho])
        index += tamanho

    # Contar quantos navios ainda não foram totalmente afundados
    navios_restantes = 0
    for navio in navios:
        if not all(coordenada in jogadas for coordenada in navio):
            navios_restantes += 1

    return navios_restantes


def gerar_mapa():
    mapa_final = []  # Aqui ficam todas as coordenadas dos barcos
    tamanhos = [1, 1, 2, 2, 3, 4, 5]  # Tamanhos dos barcos

    # Função que gera coordenadas aleatórias
    def coordenada():
        return random.randint(0, 9), random.randint(0, 9)

    # Função que determina as direções válidas para o barco
    def sentido(tamanho, pos):
        direcoes = []
        if 10 - pos[1] >= tamanho:  # Direita
            direcoes.append('Direita')
        if pos[1] >= tamanho:  # Esquerda
            direcoes.append('Esquerda')
        if 10 - pos[0] >= tamanho:  # Baixo
            direcoes.append('Baixo')
        if pos[0] >= tamanho:  # Cima
            direcoes.append('Cima')
        return random.choice(direcoes) if direcoes else None

    # Função que cria o barco baseado na direção e tamanho
    def gerar_coordenadas(tamanho, direcao, p):
        coordenadas = []
        if direcao == 'Cima':
            for a in range(tamanho):
                coordenadas.append((p[0] - a, p[1]))
        elif direcao == 'Baixo':
            for b in range(tamanho):
                coordenadas.append((p[0] + b, p[1]))
        elif direcao == 'Esquerda':
            for c in range(tamanho):
                coordenadas.append((p[0], p[1] - c))
        elif direcao == 'Direita':
            for d in range(tamanho):
                coordenadas.append((p[0], p[1] + d))
        return coordenadas

    for tamanho in tamanhos:
        while True:
            pos = coordenada()  # Gera uma posição inicial aleatória
            direcao = sentido(tamanho, pos)  # Escolhe uma direção válida
            if direcao:
                novo_barco = gerar_coordenadas(tamanho, direcao, pos)
                if all(coord not in mapa_final for coord in novo_barco): # Verifica se alguma coordenada está ocupada
                    mapa_final.extend(novo_barco)  # Adiciona as coordenadas ao mapa
                    break

    return mapa_final


def jogada(tabuleiro, mapa, linha, coluna): #OK

    if 0 <= linha < 10 and 0 <= coluna < 10 and tabuleiro[linha][coluna] == '~':

        for i in mapa:
            if linha == i[0] and coluna == i[1]:
                tabuleiro[linha][coluna] = 'X'
                print('Acertou um navio!')
                break
        else:
            tabuleiro[linha][coluna] = 'O'
            print('Água!')
       
        return tabuleiro, True

    else:
        print('==================================================')
        print('!!! Entrada Inválida, Tente Novamente !!!')
        print('==================================================')
        return tabuleiro, False


def main():
    tabuleiro = [["~" for _ in range(10)] for _ in range(10)]

    tentativas = menu_dificuldade()    

    jogadas = []

    mapa = gerar_mapa()
    print('================================================================================================================================================')
    print(f'Mapa Coordenadas para Testes\n{mapa}')
    print('================================================================================================================================================\n')

    while conferir_vitoria(mapa, jogadas) == False and conferir_derrota(tentativas) == False:
       
        print('    A    B    C    D    E    F    G    H    I    J')
        for i, j in enumerate (tabuleiro):
            print(i, j)

        try:
            linha = ord(input('\nEscolha uma Linha (A-J) ').upper()) - ord('A')
            coluna = int(input('\nEscolha uma Coluna (0-9) '))
        except:
            print('==================================================')
            print('!!! Entrada Inválida, Tente Novamente !!!')
            print('==================================================')
            continue

        limpar_terminal()

        tabuleiro, validade = jogada(tabuleiro, mapa, coluna, linha)
       
        if validade == True:
            jogadas.append((linha, coluna))
            tentativas -= 1

        print(f'Tentativas Restantes: {tentativas}')
        navios_faltando = navios_restantes(mapa, jogadas)
        print(f"Navios Restantes: {navios_faltando}")

if __name__ == '__main__':
    main()