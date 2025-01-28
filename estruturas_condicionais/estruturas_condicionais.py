# Solicita ao usuário que insira um número inteiro
primeiro_numero = int(input('Digite um número inteiro: '))

# Verifica se o número é positivo, negativo ou zero
if primeiro_numero > 0:
    print(f'O número {primeiro_numero} é positivo.')
elif primeiro_numero < 0:
    print(f'O número {primeiro_numero} é negativo.')
else:
    print('O número que você digitou é zero.')

# Solicita ao usuário que insira outro número inteiro
segundo_numero = int(input('Digite outro número inteiro: '))

# Verifica se o número é par ou ímpar
if segundo_numero % 2 == 0:
    print(f'O número {segundo_numero} é par.')
else:
    print(f'O número {segundo_numero} é ímpar.')

# Solicita ao usuário que insira dois valores
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# Compara os dois valores para verificar se são iguais ou diferentes
if primeiro_valor != segundo_valor:
    print(f'O valor {primeiro_valor} é diferente de {segundo_valor}.')
else:
    print(f'O valor {primeiro_valor} é igual a {segundo_valor}.')
