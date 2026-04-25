perguntas = [
    ['Seu animal gosta de bananas', 'macaco'],
    ['Seu animal vive na água', 'baleia'],
    ['Seu animal tem asas', 'pássaro'],
    ['Seu animal é um felino', 'leão'],
    ['Seu animal é um mamífero', 'cachorro'],
    ['Seu animal é um réptil', 'cobra'],
    ['Seu animal é um inseto', 'formiga'],
    ['Seu animal é um anfíbio', 'sapo'],
    ['Seu animal é um roedor', 'rato'],
    ['Seu animal é um animal de estimação', 'gato'],
    ['Seu animal é um animal selvagem', 'tigre'],
    ['Seu animal é um animal de fazenda', 'vaca'],
    ['Seu animal é um animal marinho', 'tubarão'],
    ['Seu animal é um animal voador', 'águia'],
    ['Seu animal é um animal de grande porte', 'elefante'],
    ['Seu animal é um animal de pequeno porte', 'hamster'],
    ['Seu animal é um animal doméstico', 'coelho'],
    ['Seu animal é um animal selvagem que vive na floresta', 'urso'],
    ['Seu animal é um animal que vive no deserto', 'camelo'],
    ['Seu animal é um animal que vive na savana', 'girafa'],
    ['Seu animal é um animal que vive na tundra', 'urso polar'],
    ['Seu animal é um animal que vive na montanha', 'cabra'],
    ['Seu animal é um animal que vive na cidade', 'pombo'],
    ['Seu animal é um animal que vive no campo', 'ovelha']
]

print('Pense em um animal e eu tentarei adivinhar qual é!')

acertou = False

for pergunta, animal in perguntas:
    resposta = input(pergunta + ' (sim/não): ').lower()

    if resposta == 'sim':
        print('Eu acho que é...', animal)
        
        confirmacao = input('Acertei? (sim/não): ').lower()
        
        if confirmacao == 'sim':
            print('Boa 😎')
            acertou = True
            break

if not acertou:
    print('Poxa, não consegui adivinhar! Você venceu!')