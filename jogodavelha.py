#jogo da velha bem simpleszinho
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

jogador = 'X'

def exibirTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('------')

def jogada(linha, coluna):
    if tabuleiro[linha][coluna] != ' ':
        print('jogada inválida.')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

def TemVencedor():
    """Verifica as linhas"""
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and    
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'O jogador {tabuleiro[linha][0]} GANHOOOOU!')
            return True 
     

    """Verifica as colunas"""
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != ' ' and    
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'O jogador {tabuleiro[0][coluna]} GANHOOOOU!')
            return True 
        
    '''Verifica as diagonais'''
    if (
        tabuleiro[0][0] != ' ' and    
        tabuleiro[0][0] == tabuleiro[1][1] and
        tabuleiro[0][0] == tabuleiro[2][2]
    ):
        print(f'O jogador {tabuleiro[0][0]} GANHOOOOU!')
        return True    

    #Se não teve ganhador e nenhuma forma
    return False
 
while True:
    print(f'É a vez do jogador {jogador}')
    try:
       linha = int(input('Digite a linha: '))
       coluna = int(input('Digite a coluna: '))
       jogador = jogada(linha, coluna)
    except (IndexError):
       print('Os valores devem ser números entre 0 e 2.')
    except ValueError:
         print('Os valores devem ser números inteiros twin. ')  
    exibirTabuleiro() 
    if TemVencedor(): 
        break  
