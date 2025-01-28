#Denindo variáveis iniciais.

nome = input('Digite seu nome: ') # Recebendo nome do usuário.

print(f'Olá, {nome}! Seja bem-vindo(a) ao teste de variáveis.') # Dando boas vindas ao usuário

# Definindo idade e verificando se é maior ou menor de idade.

idade = int(input('Digite sua idade: ')) # Recebendo idade do usuário.
maior_de_idade = idade >= 18 # Verificando maior idade.

print(f'Você é maior de idade? {maior_de_idade}') #Retornando resultado da maior idade em boolean.

# Cálculos.

num1 = int(input('Digite um número inteiro: ')) # Recebendo o primeiro número inteiro.
num2 = int(input('Digite outro número inteiro: ')) # Recebendo o segundo número inteiro.

soma =  num1 + num2 # Fazendo a soma dos números recebidos.
subtracao = num1 - num2 # Fazendo a subtração dos números recebidos.
divisao = num1 / num2 # Fazendo a divisão dos números recebidos.
multiplicacao = num1 * num2 # Fazendo a multiplicação dos números recebidos.

print(f'A soma de {num1} + {num2} é = {soma}') # Retornando o resultado da soma.
print(f'A subtração de {num1} - {num2} é = {subtracao}') # Retornando o resultado da subtração.
print(f'A divisão de {num1} / {num2} é = {divisao}') # Retornando o resultado da divisão.
print(f'A multiplicação de {num1} * {num2} é = {multiplicacao}') # Retornando o resultado da multiplicação.
