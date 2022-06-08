# ainda não fiz o código dos pedidos

def start():
    interacoes.printar_opcoes('pedidos')
    
    opcao = interacoes.pegar_opcao()
    if opcao is None:
        return

    if opcao == '1':
        gerar_pedido()
    elif opcao == '2':
        cancelar_pedido()
    elif opcao == '3':
        confirmar_pedido()

def gerar_pedido():
    cpf_cliente = input('Insira cpf do cliente: ')

