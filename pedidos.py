import database as bd
import interacoes

def start():
    interacoes.printar_opcoes_pedidos()
    
    opcao = interacoes.pegar_opcao()
    if opcao is None:
        return
    elif opcao == '4':
        interacoes.printar_lista_pedidos()

    if opcao == '1':
        gerar_pedido()
    elif opcao == '2':
        cancelar_pedido()
    elif opcao == '3':
        confirmar_pedido()


def gerar_pedido():
    cpf_cliente = input('Insira cpf do cliente: ')
    if cpf_cliente not in bd.clientes:
        interacoes.printar_nao_encontrou_cpf(cpf_cliente)
        return

    interacoes.printar_lista_produtos()

    produto = input('Insira o nome do produto: ')
    if produto not in bd.produtos:
        interacoes.printar_nao_encontrou_prod(produto)
        return

    interacoes.printar_produto(produto)

    # QUANTIDADE DO PRODUTO
    while True:
        qntd = int(input('Insira a quantidade que deseja comprar: '))

        if 0 < qntd <= bd.produtos[produto]['qntd']:
            break
        else:
            print('Quantidade inválida, tente novamente')
            continue

    # CUSTO DOS PRODUTOS
    custo = qntd * bd.produtos[produto]['preco']

    bd.pedidos.append({'cpf' : cpf_cliente,
                       'produto' : produto,
                       'qntd' : qntd,
                       'custo' : custo})

    print('\nPedido gerado! Aguardando confirmação.')

def cancelar_pedido():
    # se lista estiver vazia
    if len(bd.pedidos) == 0:
        print('Não há pedidos para cancelar')
        return

    # mostra lista de pedidos
    interacoes.printar_lista_pedidos()


    while True:
        ID = int(input('ID do pedido à cancelar: '))
        pedido = None

        try:
            pedido = bd.pedidos[ID]
        except:
            print('ID Inválido, tente novamente')
            continue

        if pedido is not None:
            break

    opcao = input('Deseja cancelar o pedido ' + str(ID) + ' (s/n)? ')
    if opcao == 's':
        print('\nPedido cancelado.')
        bd.pedidos.pop(ID)
    else:
        print('\nPedido não foi cancelado.')
        return


def confirmar_pedido():
    # se lista estiver vazia
    if len(bd.pedidos) == 0:
        print('Não há pedidos para confirmar')
        return

    # mostra lista de pedidos
    interacoes.printar_lista_pedidos()

    while True:
        ID = int(input('ID do pedido à confirmar: '))
        pedido = None

        try:
            pedido = bd.pedidos[ID]
        except:
            print('ID Inválido, tente novamente')
            continue

        if pedido is not None:
            break

    opcao = input('Deseja confirmar o pedido ' + str(ID) + ' (s/n)? ')

    if opcao == 's':
        print('\nPedido ' + str(ID) + ' confirmado!')
        bd.produtos[pedido['produto']]['qntd'] -= pedido['qntd']
        bd.pedidos.pop(ID)
    else:
        print('\nPedido não foi confirmado')
        return