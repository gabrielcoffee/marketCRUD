import sys
import interacoes
import clientes
import produtos
import vendas
import database as bd
import json

def iniciar():
    while True:
        interacoes.printar_menu()

        opcao = input(interacoes.RED + '\n--> ' + interacoes.RESET)

        if opcao == '1':
            clientes.start()
        elif opcao == '2':
            produtos.start()
        elif opcao == '3':
            vendas.start()
        elif opcao == '4':
            print('Fechando programa...')
            sys.exit()

        salvar_bd()

def salvar_bd():
    # dicionário que será salvo em json
    bd_total = {
        'clientes' : bd.clientes,
        'produtos' : bd.produtos,
        'vendas' : bd.vendas
    }

    # salva o dicionario do banco de dados em json
    with open('database.json', 'w') as outfile:
        json.dump(bd_total, outfile)

def resgatar_bd():
    with open('database.json', 'r') as json_file:

        # tenta carregar os dados do arquivo sem dar erro ( try, except )
        try:
            dados = json.load(json_file)
        except:
            return

        if dados is not None:
            bd.clientes = dados['clientes']
            bd.produtos = dados['produtos']
            bd.vendas = dados['vendas']

if __name__ == '__main__':
    interacoes.printar_inicio()
    resgatar_bd()
    iniciar()