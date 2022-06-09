import database as bd


def printar_inicio():
    print('===========================================')
    print('Grupo: Os trava python')
    print('Alunos: Angelo, Lohan, Leonardo, Gabriel F.')
    print('Sistema de clientes, produtos e pedidos')
    print('===========================================')


def printar_menu():
    print('\n===== MENU =====')
    print('1. Clientes')
    print('2. Produtos')
    print('3. Pedidos')
    print('4. Salvar e SAIR')


def printar_opcoes(opcao_tipo):
    print('\n1. Adicionar ' + opcao_tipo)
    print('2. Remover ' + opcao_tipo)
    print('3. Editar ' + opcao_tipo)
    print('4. Pesquisar ' + opcao_tipo)
    print('5. Lista de ' + opcao_tipo + 's')
    print('Enter: Voltar ao menu\n')


def printar_opcoes_pedidos():
    print('\n1. Gerar pedido')
    print('2. Cancelar pedido')
    print('3. Confirmar pedido')
    print('4. Lista de pedido' + 's')
    print('Enter: Voltar ao menu\n')


def printar_nao_encontrou_cpf(cpf):
    print('\nCPF: ' + cpf + ' não consta na lista dos cpf de clientes...')


def printar_nao_encontrou_prod(prod):
    print('\nProduto: ' + prod + ' não consta na lista de produtos...')


def printar_lista_produtos():
    if len(bd.produtos) == 0:
        print('\nLista de produtos está vazia')
        return

    print('LISTA DE PRODUTOS:\n')
    # printa cada produto
    for prod in bd.produtos.keys():
        printar_produto(prod)
        print()


def printar_lista_clientes():
    if len(bd.clientes) == 0:
        print('\nLista de clientes está vazia')
        return

    print('LISTA DE CLIENTES:\n')
    # printa cada cliente
    for cpf in bd.clientes.keys():
        printar_cliente(cpf)
        print()


def printar_lista_pedidos():
    if len(bd.pedidos) == 0:
        print('\nLista de pedidos está vazia')
        return

    print('LISTA DE PEDIDOS:\n')
    # printa cada cliente
    for i in range(len(bd.pedidos)):
        printar_pedido(i)
        print()


def pegar_opcao():
    opcao = input('Opção: ')
    print()
    if opcao == '':
        print('Voltando ao menu')
        return None
    else:
        return opcao


def printar_item_adicionado(item_tipo, item_nome):
    print('\n' + item_tipo + ' "' + item_nome + '" adicionado!')


def printar_cliente(cpf):
    print('cliente: ' + bd.clientes[cpf]['nome'])
    print('cpf: ' + cpf)
    print('número: ' + bd.clientes[cpf]['num'])
    print('endereço: ' + bd.clientes[cpf]['end'])


def printar_produto(prod):
    print('produto: ' + prod)
    print('quantidade: ' + str(bd.produtos[prod]['qntd']))
    print('preço: ' + '{:.2f}'.format(bd.produtos[prod]['preco']))
    print('descrição : ' + bd.produtos[prod]['desc'])


def printar_pedido(ID):
    pedido = bd.pedidos[ID]
    print('Número ID do pedido: ' + str(ID))
    print('CPF do cliente: ' + pedido['cpf'])
    print('Produto(s): ' + str(pedido['qntd']) + ' ' +  pedido['produto'])
    print('Custo: ' + '{:.2f}'.format(pedido['custo']))