import sys
import interacoes
import clientes
import produtos
import pedidos

def iniciar():
    while True:
        interacoes.printar_menu()

        opcao = input('\nEscolha uma das opções: ')

        if opcao == '1':
            clientes.start()
        elif opcao == '2':
            produtos.start()
        elif opcao == '3':
            pedidos.start()
        elif opcao == '4':
            registrar_bd()
            sys.exit()

def registrar_bd():
    print('Salvando registros...')
    print('Fechando programa...')

if __name__ == '__main__':
    interacoes.printar_inicio()
    iniciar()