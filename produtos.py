import database as bd
import interacoes

def start():
    interacoes.printar_opcoes('produto')

    opcao = input('Opção: \n')
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
        print('Opção inválida, voltando ao menu...')
        return

    if opcao == '5':
        interacoes.printar_lista_produtos()
        return

    interacoes.printar_acao(opcao, 'produto')
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
    if produto in bd.produtos.keys():
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

    bd.produtos[produto] = {
        'qntd' : qntd,
        'preco' : preco,
        'desc' : desc
    }

    interacoes.printar_item_adicionado('Produto', produto)

def remover(produto):
    if produto not in bd.produtos.keys():
        interacoes.printar_nao_encontrou_prod(produto)
    else:
        bd.produtos.pop(produto)

def editar(produto):
    if produto not in bd.produtos.keys():
        interacoes.printar_nao_encontrou_prod(produto)
    else:
        # pega valores atuais
        nome = produto
        qntd = bd.produtos[produto]['qntd']
        preco = bd.produtos[produto]['preco']
        desc = bd.produtos[produto]['desc']

        while True:
            print('===== VALORES ATUAIS =====')
            print('1. Nome: ' + produto)
            print('2. Quantidade: ' + str(qntd))
            print('3. Preço: ' + '{:.2f}'.format(preco))
            print('4. Descrição: ' + desc)
            print('5. CANCELAR EDIÇÃO')

            opcao = input('\nO que deseja editar? ')

            if opcao == '1':
                nome = input('Novo nome: ')
            elif opcao == '2':
                qntd = int(input('Nova quantidade'))
            elif opcao == '3':
                preco = float(input('Novo preço: '))
            elif opcao == '4':
                desc = input('Nova descrição: ')
            elif opcao == '5':
                break

            # mudou nome do produto
            if nome != produto:
                bd.produtos.pop(produto)

            # atualiza cliente
            bd.produtos[nome] = {
                'qntd': qntd,
                'preco' : preco,
                'desc' : desc
            }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 's':
                produto = nome
                continue
            else:
                break

def pesquisar(prod):
    if prod not in bd.produtos.keys():
        interacoes.printar_nao_encontrou_prod(prod)
    else:
        interacoes.printar_produto(prod)