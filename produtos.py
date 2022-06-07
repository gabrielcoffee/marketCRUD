from main import produtos_bd
from interacoes import printar_opcoes, printar_nao_encontrou_prod

def start():
    printar_opcoes('produtos')

    opcao = input('Opção: ')
    produto = input('Nome do produto: ')

    if opcao == '1':
        adicionar(produto)
    elif opcao == '2':
        remover(produto)
    elif opcao == '3':
        editar(produto)
    elif opcao == '4':
        pesquisar(produto)


def adicionar(produto):
    # se produto ja estiver no dicionario...
    if produto in produtos_bd.keys():
        opcao = input('Esse produto ja esta cadastrado, deseja edita-lo (s/n): ')
        if opcao == 's':
            editar(produto)
            return
        else:
            return

    # se produto não estiver no dicionario...
    preco = input('Preço do produto: ')
    desc = input('Descrição do produto: ')

    produtos_bd[produto] = {
        'preco' : preco,
        'desc'  : desc
    }

def remover(produto):
    if produto not in produtos_bd.keys():
        printar_nao_encontrou_prod(produto)
    else:
        produtos_bd.pop(produto)

def editar(produto):
    if produto not in produtos_bd.keys():
        printar_nao_encontrou_prod(produto)
    else:
        # pega valores atuais
        preco = produtos_bd[produto]['preco']
        desc = produtos_bd[produto]['desc']

        while True:
            print('===== VALORES ATUAIS =====')
            print('1. Preço: ' + preco)
            print('2. Descrição: ' + desc)
            print('3. CANCELAR EDIÇÃO')

            opcao = input('\nO que deseja editar? ')

            if opcao == 1:
                preco = input('Novo preço: ')
            elif opcao == 2:
                desc = input('Nova descrição: ')
            elif opcao == 3:
                break

            # atualiza cliente
            produtos_bd[produto] = { 'preco' : preco, 'desc' : desc }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 'n':
                break
            elif opcao == 's':
                continue

def pesquisar(produto):
    if produto not in produtos_bd.keys():
        printar_nao_encontrou_prod(produto)
    else:
        produto = produtos_bd[produto]
        print('\n=== produto ===')
        print('Preço: ' + produto['preco'])
        print('Descrição: ' + produto['desc'])

def printar_lista():
    if len(produtos_bd) == 0:
        print('\nLista de produtos está vazia\n')
        return

    print('LISTA DE PRODUTOS:\n')
    for prod in produtos_bd.keys():
        print()
        print('preço: ' + produtos_bd[prod]['preco'])
        print('descrição : ' + produtos_bd[prod]['desc'])