import sys
import interacoes
import clientes
import produtos
import pedidos
import database as bd
import json

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
    print('\nSalvando registros...')

    # dicionário que será salvo em json
    bd_total = {
        'clientes' : bd.clientes,
        'produtos' : bd.produtos,
        'pedidos' : bd.pedidos
    }

    # salva o dicionario do banco de dados em json
    with open('database.json', 'w') as outfile:
        json.dump(bd_total, outfile)

    print('Fechando programa...')

def resgatar_bd():
    print('\nResgatando registros...')
    with open('database.json', 'r') as json_file:

        # tenta carregar os dados do arquivo sem dar erro ( try, except )
        try: dados = json.load(json_file)
        except: return

        if dados is not None:
            bd.clientes = dados['clientes']
            bd.produtos = dados['produtos']
            bd.pedidos = dados['pedidos']

if __name__ == '__main__':
    interacoes.printar_inicio()
    resgatar_bd()
    iniciar()