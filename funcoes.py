#Código apenas para entender 
def Olamundo():
    print('Apenas um teste')

Olamundo() 

#Código mais avançado para dar saudações ao usuário e dobrar um número fornecido por ele
nome = input('Qual é o seu nome? ')

def Saudacao(nome):
    print('Olá, ' + nome + '! Bem-vindo(a)!')
Saudacao(nome)

#Código para dobrar um número fornecido pelo usuário
input('Digite um número aleatório e ele será dobrado!')

def Dobro(numero):
    return numero * 2
numero = int(input('Digite um número: '))
resultado = Dobro(numero)   
print('O dobro de', numero, 'é', resultado)