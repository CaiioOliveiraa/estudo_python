# Script para coletar nome do usuário e exibir informações detalhadas
# Caso não digite, será exibida uma mensagem de erro

# Solicita o nome do usuário
nome = input('Digite seu nome: ')

# Verifica se o campos foi preenchidos
if nome:
    # Exibe o nome do usuário
    print(f'Seu nome é {nome}')
    
    # Exibe o nome do usuário invertido
    print(f'Seu nome invertido é {nome[::-1]}')
    
    # Verifica se o nome contém espaços
    if ' ' in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome NÃO contém espaço.')
    
    # Exibe a quantidade de caracteres no nome
    print(f'Seu nome tem {len(nome)} letras.')
    
    # Exibe a primeira letra do nome
    print(f'A primeira letra do seu nome é {nome[0]}')
    
    # Exibe a última letra do nome
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    # Exibe uma mensagem de erro caso algum campo esteja vazio
    print('Desculpe, você NÃO digitou seu nome.')
