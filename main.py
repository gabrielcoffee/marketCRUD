import sys
import interacoes
import database as bd

def iniciar():
    import clientes
    import produtos

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
            registrar_bd()
            sys.exit()

def registrar_bd():
    print('Salvando registros...')

if __name__ == '__main__':
    interacoes.printar_inicio()
    iniciar()