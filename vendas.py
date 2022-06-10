import database as bd
import interacoes

def start():
    interacoes.printar_opcoes_compras()

    opcao = input('Opção: ')
    print()

    if opcao != '1' and opcao != '2':
        print('Opção inválida, voltando ao menu...')
        return

    if opcao == '1':
        gerar_compra()
    elif opcao == '2':
        interacoes.printar_lista_vendas()


def gerar_compra():

    cpf_cliente = input('Insira cpf do cliente: ')
    if cpf_cliente not in bd.clientes:
        interacoes.printar_nao_encontrou_cpf(cpf_cliente)
        return

    print('Cliente: ' + bd.clientes[cpf_cliente]['nome'] + '\n')

    interacoes.printar_lista_produtos()

    produtos_qntd = {}
    while True:
        pular_prod = False
        while True:

            print('(Enter para não adicionar mais produtos)')
            produto = input('Insira o nome do produto: ')
            if produto == '':
                pular_prod = True
                break

            elif produto not in bd.produtos:
                interacoes.printar_nao_encontrou_prod(produto)
                print('Tente novamente...\n')
                continue

            elif bd.produtos[produto]['qntd'] == 0:
                pular_prod = True
                print('Produto esgotado\n')
                break
            else:
                break

        if pular_prod == False:
            print('\nPRODUTO SELECIONADO: ')
            interacoes.printar_produto(produto)
            print()

            while True:
                qntd = int(input('Insira a quantidade que deseja comprar: '))

                if 0 < qntd <= bd.produtos[produto]['qntd']:
                    break
                else:
                    print('Quantidade inválida, tente novamente')
                    continue

            produtos_qntd[produto] = qntd
            if qntd == 1:
                print('Uma unidade do produto ' + produto + ' adicionada ao carrinho!')
            else:
                for prod in produtos_qntd.keys():
                    bd.produtos[prod]['qntd'] -= produtos_qntd[prod]
                print(str(qntd) + ' unidades do produto ' + produto + ' adicionadas ao carrinho!')


        # FIM DA COMPRA
        cancelar = False
        opcao = input('Deseja escolher outros produtos (s/n)? ')
        if opcao == 's':
            continue
        else:
            if len(produtos_qntd) == 0:
                cancelar = True
                print('Carrinho está vazio. Venda cancelada.')
            break

    # FORA DO LOOP DE COMPRA
    if cancelar == True:
        for prod in produtos_qntd.keys():
            bd.produtos[prod]['qntd'] += produtos_qntd[prod]
        return

    print('PEDIDO:')
    interacoes.printar_produtos_selecionados_e_total(produtos_qntd)
    opcao = input('Deseja confirmar a venda (s/n)?')
    if opcao == 's':
        # adiciona a lista de compras
        bd.vendas.append({'cpf': cpf_cliente,
                          'produtos_qntd': produtos_qntd
                          })
    else:
        for prod in produtos_qntd.keys():
            bd.produtos[prod]['qntd'] += produtos_qntd[prod]
        print('Venda cancelada.')