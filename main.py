from interacoes import printar_inicio, printar_menu
import json

# "BANCO DE DADOS"
clientes_bd = { 123 : { 'gab', 999, 'casa1' },
                234 : { 'ang', 987, 'casa2' }
                }
produtos_bd = {}
bd = {}

def iniciar():
    import clientes
    import produtos

    while True:
        printar_menu()

        opcao = input('\nEscolha uma das opções: ')

        if opcao == '1':
            clientes.start()
        elif opcao == '2':
            clientes.printar_lista()
        elif opcao == '3':
            produtos.start()
        elif opcao == '4':
            produtos.printar_lista()
        elif opcao == '5':
            registrar_bd()

        # atualiza bd
        bd['clientes'] = clientes_bd
        bd['produtos'] = produtos_bd

def registrar_bd():
    json_string = json.dumps(bd)
    print(json_string)

if __name__ == '__main__':
    printar_inicio()
    try:
        bd = json.loads('bd.json')
    except:
        print('\nBanco de dados não foi encontrado ou está vazio')
    iniciar()