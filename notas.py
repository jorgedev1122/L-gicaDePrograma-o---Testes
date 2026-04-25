#código com if e else
nota = int(input('digite sua nota: '))

if nota >= 7:
    print('aprovado')
else: 
    if nota < 5:
        print('reprovado')
    else:    
         print('está em recuperação')

#código com elif
nota = int(input('Digite sua nota: '))

if nota >=7:
    print('Passou!!!!')
elif nota < 5:
    print('Não passou! :(')
else:
    print('Recuperação')