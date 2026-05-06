def calcular_media(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]  

    media = soma / len(numeros)
    return media


def maior_numero(lista):
    maior = 0
    for n in lista:
        if n > maior:
            maior = n  

    return maior


def main():
    numeros = [5, 10, 15, 20]

    media = calcular_media(numeros)
    print("Média:", media)

    maior = maior_numero(numeros)
    print("Maior número:", maior)

    if media > 10:
        print("Média alta")
    else:
        print("Média baixa")


main()