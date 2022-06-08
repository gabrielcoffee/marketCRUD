import sys
import interacoes
import database as bd

def iniciar():
    import clientes
    import produtos
    import pedidos

    while True:
        interacoes.printar_menu()

        opcao = input('\nEscolha uma das opções: ')

        if opcao == '1':
            clientes.start()
        elif opcao == '2':
            interacoes.printar_dict(bd.clientes, 'clientes')
        elif opcao == '3':
            produtos.start()
        elif opcao == '4':
            interacoes.printar_dict(bd.produtos, 'produtos')
        elif opcao == '5':
            pedidos.start()
        elif opcao == '6':
            interacoes.printar_dict(bd.pedidos, 'pedidos')
        elif opcao == '7':
            registrar_bd()
            sys.exit()

def registrar_bd():
    print('Salvando registros...')
    print('Fechando programa...')

if __name__ == '__main__':
    interacoes.printar_inicio()
    iniciar()