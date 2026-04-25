#código simples utilizando and, or e not
print('hoje vamos dirigir?')
tempo = input('como está o tempo? (chuvoso, ensolarado, nublado): ')
if tempo == 'chuvoso':
    print('melhor não dirigir, pode ser perigoso!')
elif tempo == 'ensolarado' and tempo == 'nublado':
    print('ótimo, pode dirigir!')