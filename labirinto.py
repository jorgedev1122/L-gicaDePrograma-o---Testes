import random
def garantir_caminho(labirinto, tamanho):
    """Abre um trajeto aleatorio entre o inicio e a chegada."""
    linha = coluna = 0
    labirinto[linha][coluna] = 0

    while linha < tamanho - 1 or coluna < tamanho - 1:
        movimentos = []
        if linha < tamanho - 1:
            movimentos.append((1, 0))
        if coluna < tamanho - 1:
            movimentos.append((0, 1))

        mover_linha, mover_coluna = random.choice(movimentos)
        linha += mover_linha
        coluna += mover_coluna
        labirinto[linha][coluna] = 0

def criar_labirinto(tamanho): #criar labirinto com tamanho definido pelo usuário
    labirinto = [ [ random.randint(0, 1) for _ in range(tamanho) ] for _ in range(tamanho) ] #criação do labirinto utilizando a biblioteca random para gerar números aleatórios entre 0 e 1, onde 0 representa um caminho livre e 1 representa uma parede
    garantir_caminho(labirinto, tamanho)
    labirinto[0][0] = '웃' #primeira posição do labirinto é o ponto de partida, representado pelo bonequinho
    labirinto[tamanho - 1][tamanho - 1] = '🏁' #última posição do labirinto é o ponto de chegada, representado pela bandeira
    return labirinto #Só retona o labirinto

def exibir_labirinto(labirinto):
    for linha in labirinto:
        print(linha)

def nao_pode_seguir(labirinto, linha, coluna):
    if (linha >= len(labirinto) or
        coluna >= len(labirinto) or
        linha < 0 or #comando para quando a posição estiver fora do labirinto, o computador não consiga seguir  
        coluna < 0 or #comando para quando a posição estiver fora do labirinto, o computador não consiga seguir
        labirinto[linha][coluna] == 1 or
        labirinto[linha][coluna] == 2): #comando para não seguir por posições que já foram exploradas, representadas pelo 2
        return True

def explorar(labirinto, linha, coluna):
    print(f"Explorando posição ({linha}, {coluna})")
    if nao_pode_seguir(labirinto, linha, coluna):
        print(f"Não é possível seguir por ({linha}, {coluna})")
        return False
    if labirinto[linha][coluna] == '🏁': #verifica se a posição é o ponto de chegada
        print(f"Chegou ao destino ({linha}, {coluna})")
        return True

    #marcar posição já explorada
    labirinto[linha][coluna] = 2 #marca a posição como explorada, representada pelo 2

    return (
        explorar(labirinto, linha, coluna + 1) or #direita
        explorar(labirinto, linha + 1, coluna) or #baixo 
        explorar(labirinto, linha, coluna - 1) or #esquerda
        explorar(labirinto, linha - 1, coluna) #cima        
    )

lab = criar_labirinto(5)
exibir_labirinto(lab)     

explorar(lab, 0, 0)