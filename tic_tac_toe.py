def mostrar_tabuleiro(board):
    print()
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("\n-------------------------")
        if (i) % 3 == 0 or i == 0:
            print(f"   {board[i]} ", end='  ')
        else:
            print(f"|   {board[i]} ", end='  ')
    print('\n \n========================')


def confere_resultado(board):

    #Empate
    if board.count('X') == 5:
        mostrar_tabuleiro(board)
        print("         Empate")
        return True

    #Linhas
    for i in range(0, 9, 3):
        if board[i] == 'O' and board[i+1] == 'O' and board[i+2] == 'O':
            print("     Jogador Campeão")
            return True
        if board[i] == 'X' and board[i+1] == 'X' and board[i+2] == 'X':
            mostrar_tabuleiro(board)
            print("       CPU Campeã - Linha")
            return True


    #Colunas
    for j in range(3):
        if board[j] == 'O' and board[j+3] == 'O' and board[j+6] == 'O':
            print("     Jogador Campeão")
            return True
        if board[j] == 'X' and board[j+3] == 'X' and board[j+6] == 'X':
            mostrar_tabuleiro(board)
            print("       CPU Campeã - Coluna")
            return True

    #Diagonais
    if board[0] == 'X' and board[4] == 'X' and board[-1] == 'X':
        mostrar_tabuleiro(board)
        print("       CPU Campeã - Diagonal")
        return True
    
    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        mostrar_tabuleiro(board)
        print("       CPU Campeã - Diagonal")
        return True


def movimento_jogador(board):
    mov = int(input('\n\n Faça seu Movimento: '))
    if mov in board:
        board.insert(mov, 'O')
        board.pop(mov-1)
        return board
    else:
        print('   Posição Inválida')
        mostrar_tabuleiro(board)
        movimento_jogador(board)


def movimento_cpu(board):
    from random import randrange
    mov = randrange(9)
    if mov in board:
        board.insert(mov, 'X')
        board.pop(mov-1)
        print("      Movimento CPU")
        return board
    else:
        movimento_cpu(board)


def main():
    game = [1, 2, 3, 4, 'X', 6, 7, 8, 9]
    
    while confere_resultado(game) != True:
        mostrar_tabuleiro(game)
        movimento_jogador(game)
        mostrar_tabuleiro(game)

        if confere_resultado(game) != True:
            movimento_cpu(game)
    else:
        print('\n       Fim do Jogo')
        print('\n   Outra Partida (S/N)')
        opcao = input(" Insira sua Resposta: ")
        if opcao == 'S' or opcao == 's':
            opcao = None
            main()

main()