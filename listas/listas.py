# Script que permite ao usuário adicionar, remover e visualizar itens de uma lista de compras com tratamento de erros.

# Inicializa a lista de compras
lista_compras = []

# Inicia o loop principal para interação com o usuário
while True:
    try:
        # Solicita ao usuário que escolha uma opção
        escolha = input('Escolha uma opção \n' +
                        '1 - Adicionar item à lista \n' +
                        '2 - Remover item da lista \n' +
                        '3 - Visualizar itens da lista \n' +
                        '4 - Sair \n' +
                        '>>> ')
        # Converte a escolha para um número inteiro
        escolha_int = int(escolha)

        # Verifica se a escolha é válida (deve ser 1, 2, 3 ou 4)
        if escolha_int not in [1, 2, 3, 4]:
            print('Digite uma opção válida.')
            continue  # Retorna ao início do loop sem executar mais nada

        # Caso a escolha seja '1', o usuário pode adicionar um item à lista
        if escolha_int == 1:
            item = input('Digite o item que deseja adicionar: ').strip()  # Pede ao usuário o item para adicionar e remove espaços extras
            if item:  # Verifica se o item não está vazio
                lista_compras.append(item)  # Adiciona o item à lista
                print(f'{item} adicionado à lista.')  # Informa que o item foi adicionado
            else:
                print('O compo item não pode estar vazio.')  # Mensagem de erro caso o item seja vazio

        # Caso a escolha seja '2', o usuário pode remover um item da lista
        elif escolha_int == 2:
            if lista_compras:  # Verifica se a lista não está vazia
                item = input('Digite o item que deseja remover: ').strip()  # Pede o item para remoção
                if item in lista_compras:  # Verifica se o item está na lista
                    lista_compras.remove(item)  # Remove o item da lista
                    print(f'{item} removido da lista.')  # Informa que o item foi removido
                else:
                    print('Item não encontrado na lista.')  # Informa se o item não está na lista
            else:
                print('A lista está vazia. Nenhum item para remover.')  # Informa se a lista está vazia

        # Caso a escolha seja '3', o usuário pode visualizar a lista
        elif escolha_int == 3:
            print('\n Lista de Compras:')
            if lista_compras:  # Verifica se a lista contém itens
                # Exibe os itens da lista com a numeração
                for i, item in enumerate(lista_compras, 1):
                    print(f'{i} - {item}')
            else:
                print('A lista está vazia.')  # Informa se a lista estiver vazia

        # Caso a escolha seja '4', o programa será encerrado
        elif escolha_int == 4:
            print('Saindo da lista...')
            break  # Sai do loop e encerra o programa

    except ValueError:
        # Caso o usuário insira algo que não seja um número, exibe uma mensagem de erro
        print('Erro: Digite um número válido!')