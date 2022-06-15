import database as bd
import interacoes


def start():
    interacoes.printar_opcoes_compras()

    opcao = input(interacoes.BLUE + 'Opção: ' + interacoes.RESET)
    print()

    if opcao != '1' and opcao != '2':
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

    produtos_qntd_preco = {}
    while True:
        pular_prod = False
        while True:

            interacoes.printar_cor('(Enter para não adicionar mais produtos)', interacoes.RED)
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
                interacoes.printar_cor('Produto esgotado\n', interacoes.RED)
                break
            else:
                break

        if pular_prod == False:
            interacoes.printar_cor('\nPRODUTO SELECIONADO: ', interacoes.GREEN)
            interacoes.printar_produto(produto)
            print()

            while True:
                qntd = int(input('Insira a quantidade que deseja comprar: '))

                if 0 < qntd <= bd.produtos[produto]['qntd']:
                    break
                else:
                    interacoes.printar_cor('Quantidade inválida, tente novamente', interacoes.RED)
                    continue

            produtos_qntd_preco[produto] = {'preco': bd.produtos[produto]['preco'], 'qntd': qntd}
            if qntd == 1:
                interacoes.printar_cor('Uma unidade do produto ' + produto + ' adicionada ao carrinho!',
                                       interacoes.GREEN)
            else:
                for prod in produtos_qntd_preco.keys():
                    bd.produtos[prod]['qntd'] -= produtos_qntd_preco[prod]['qntd']
                print(str(qntd) + ' unidades do produto ' + produto + ' adicionadas ao carrinho!')

        # FIM DA COMPRA
        cancelar = False
        opcao = input('Deseja escolher outros produtos (s/n)? ')
        if opcao == 's':
            continue
        else:
            if len(produtos_qntd_preco) == 0:
                cancelar = True
                interacoes.printar_cor('Carrinho está vazio. Venda cancelada.', interacoes.RED)
            break

    # FORA DO LOOP DE COMPRA
    if cancelar == True:
        for prod in produtos_qntd_preco.keys():
            bd.produtos[prod]['qntd'] += produtos_qntd_preco[prod]['qntd']
        return

    print('PEDIDO:')
    interacoes.printar_produtos_selecionados_e_total(produtos_qntd_preco)
    fim = False
    while True:
        opcao = input('\nDeseja finalizar a compra (s/n)?')
        if opcao == 's':
            print('Parabéns sua compra foi efetuada!')
            # adiciona a lista de compras
            bd.vendas.append({'cpf': cpf_cliente,
                              'produtos_qntd_preco': produtos_qntd_preco
                              })
            fim = True
        else:
            while True:
                opcao = input('\nDeseja cancelar a compra ou remover algum produto (c/r)? ')
                if opcao == 'c':
                    for prod in produtos_qntd_preco.keys():
                        bd.produtos[prod]['qntd'] += produtos_qntd_preco[prod]['qntd']
                    interacoes.printar_cor('Venda cancelada.', interacoes.RED)
                    fim = True
                    break
                elif opcao == 'r':
                    remov = input("Digite qual produto deseja remover: ")
                    if remov in produtos_qntd_preco.keys():
                        bd.produtos[remov]['qntd'] += produtos_qntd_preco[remov]['qntd']
                        produtos_qntd_preco.pop(remov)
                        break
                else:
                    print('Digite uma opção válida...\n')
        if fim:
            break
# def devolução:
