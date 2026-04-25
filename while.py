# Exemplo simples para entender while e for em Python

# O loop while repete um bloco de código enquanto uma condição for verdadeira
# Exemplo: Contar de 1 até 5
contador = 1  # Inicializamos o contador
while contador <= 5:  # Enquanto contador for menor ou igual a 5
    print(f"Contador: {contador}")  # Imprime o valor atual
    contador += 1  # Incrementa o contador (contador = contador + 1)

print("Fim do while\n")  # Quebra de linha para separar os exemplos

# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, string, etc.)
# Exemplo: Iterar sobre uma lista de frutas
frutas = ["maçã", "banana", "laranja"]  # Lista de frutas
for fruta in frutas:  # Para cada fruta na lista frutas
    print(f"Fruta: {fruta}")  # Imprime a fruta atual

print("Fim do for")