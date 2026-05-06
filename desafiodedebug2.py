#primeira função, contar pares
def contar_pares(lista):
    contador = 0
    
    for i in range(len(lista)):
        if lista[i] % 2 == 0:  
            contador += 1  

    return contador
#fim da função contar pares


#função para inverter um texto
def inverter_texto(texto):
    texto_invertido = ""
    
    for i in range(len(texto)-1, -1, -1):  
        texto_invertido += texto[i]  

    return texto_invertido
#fim da função inverter_texto

#função para buscar um nome em uma lista
def buscar_nome(lista, nome):
    for i in range(len(lista)):
        if lista[i] == nome:  
            return True  

    return False
#fim da função buscar_nome



#organizar main
def main():
    numeros = [1, 2, 3, 4, 5, 6]
    texto = "Hello, World!"
    nomes = ["Alice", "Bob", "Charlie"]

    pares = contar_pares(numeros)
    print(f"Números pares na lista: {pares}")

    texto_invertido = inverter_texto(texto)
    print(f"Texto invertido: {texto_invertido}")

    nome_procurado = "Bob"
    encontrado = buscar_nome(nomes, nome_procurado)
    if encontrado:
        print(f"{nome_procurado} encontrado na lista.")
    else:
        print(f"{nome_procurado} não encontrado na lista.")

main()        
#fim do programa