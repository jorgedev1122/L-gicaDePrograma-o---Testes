print('Simulador de compras de supermercado explicado linha por linha.')
produto = "arroz" #nome do produto
preço_unitário = 5.79 #preço por unidade do produto
quantidade = 3 #quantidade comprada

#Cálculo do valor total da compra
valor_total = preço_unitário * quantidade #valor total sem desconto

#Aplicando o desconto de 10% se a quantidade for maior que 2
if quantidade > 2: #verificando se a quantidade é maior que 2
    valor_total = valor_total * 0.9 #aplicando o desconto de 10% ao valor total

print("Produto:", produto) #exibindo o nome do produto
print('quantidade comprada:', quantidade) #exibindo a quantidade comprada
print("Valor total da compra: R$" + str(valor_total)) #exibindo o valor total da compra com o desconto aplicado, se houver