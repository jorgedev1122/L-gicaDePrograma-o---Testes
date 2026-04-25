print('bem vindo ao resultado do enem!')
#boas vindas ao usuário

nota = int(input('digite sua nota: '))
#função para digitar a nota do usuário

if nota == 1000:
    print('Parabéns, você tirou a nota máxima!')
#caso a nota seja igual a 1000, o código mostra que o usuário passou com a nota máxima

elif nota >= 700:
    print('Parabéns, você passou!')
#caso a nota seja maior ou igual a 700, o código mostra que o usuário passou
    
else:
    print('Infelizmente, você não passou.')
#caso a nota seja menor que 700, o código mostra que o usuário não passou

#resumidamente, o elif é usado para verificar uma condição adiona sem precisar de vários ifs elses.    