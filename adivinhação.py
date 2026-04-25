print('pensei em um número entre 1 e 10, tente adivinhar qual é!')
numero = 7
chute = int(input('Digite seu chute: '))    
if chute == numero:     
    print('Parabéns, você acertou!')
else:   
    print('Que pena, você errou! O número era', numero)