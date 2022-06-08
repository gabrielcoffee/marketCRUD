from database import produtos
import interacoes

def start():
    interacoes.printar_opcoes('produtos')

    opcao = interacoes.pegar_opcao()
    if opcao is None:
        return

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
    if produto in produtos.keys():
        opcao = input('Esse produto ja esta cadastrado, deseja edita-lo (s/n): ')
        if opcao == 's':
            editar(produto)
            return
        else:
            return

    # se produto não estiver no dicionario...
    qntd = int(input('Quantidade do produto no estoque: '))
    preco = float(input('Preço do produto: '))
    desc = input('Descrição do produto: ')

    produtos[produto] = {
        'qntd' : qntd,
        'preco' : preco,
        'desc' : desc
    }

    interacoes.printar_item_adicionado('Produto', produto)

def remover(produto):
    if produto not in produtos.keys():
        interacoes.printar_nao_encontrou_prod(produto)
    else:
        produtos.pop(produto)

def editar(produto):
    if produto not in produtos.keys():
        interacoes.printar_nao_encontrou_prod(produto)
    else:
        # pega valores atuais
        qntd = produtos[produto]['qntd']
        preco = produtos[produto]['preco']
        desc = produtos[produto]['desc']

        while True:
            print('===== VALORES ATUAIS =====')
            print('1. Quantidade: ' + qntd)
            print('2. Preço: ' + preco)
            print('3. Descrição: ' + desc)
            print('4. CANCELAR EDIÇÃO')

            opcao = input('\nO que deseja editar? ')

            if opcao == 1:
                qntd = int(input('Nova quantidade'))
            elif opcao == 2:
                preco = float(input('Novo preço: '))
            elif opcao == 3:
                desc = input('Nova descrição: ')
            elif opcao == 4:
                break

            # atualiza cliente
            produtos[produto] = {
                'qntd': qntd,
                'preco' : preco,
                'desc' : desc }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 'n':
                break
            elif opcao == 's':
                continue

def pesquisar(prod):
    if prod not in produtos.keys():
        interacoes.printar_nao_encontrou_prod(prod)
    else:
        produto = produtos[prod]
        print('\nProduto: ' + produto)
        print('Quantidade: ' + produto['qntd'])
        print('Preço: ' + produto['preco'])
        print('Descrição: ' + produto['desc'])