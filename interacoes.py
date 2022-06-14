import database as bd

""" ANSI color codes """
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\u001b[34;1m"
YELLOW = "\033[1;33m"
RESET =  "\u001b[0m"

def printar_cor(texto, color_code = RESET):
    print(color_code + texto + RESET)

# MENUS
def printar_inicio():
    print('========================')
    printar_cor('Grupo: OS TRAVA PYTHON', BLUE)
    printar_cor('Alunos: ', GREEN)
    print('   Angelo Sequinel,\n   Lohan Berg,\n   Leonardo Cavalli,\n   Gabriel Fernandes.')
    printar_cor('Sistema para mercado', BLUE)
    print('========================')

def printar_menu():
    printar_cor('\n===== MENU =====', GREEN)
    print('1. Clientes')
    print('2. Produtos')
    print('3. Compra e Vendas')
    print('4. Fechar programa')

def printar_opcoes(opcao_tipo):
    print('\n1. Adicionar ' + opcao_tipo)
    print('2. Remover ' + opcao_tipo)
    print('3. Editar ' + opcao_tipo)
    print('4. Pesquisar ' + opcao_tipo)
    print('5. Lista de ' + opcao_tipo + 's')
    printar_cor('Enter: Voltar ao menu\n', RED)

def printar_opcoes_compras():
    print('\n1. Gerar compra')
    print('2. Listar vendas')
    printar_cor('Enter: Voltar ao menu\n', RED)

def printar_acao(opcao, opcao_tipo):
    if opcao == '1':
        print('Vamos adicionar um ' + opcao_tipo + '!\n')
    elif opcao == '2':
        print('Vamos remover um ' + opcao_tipo + '!\n')
    elif opcao == '3':
        print('Vamos editar um ' + opcao_tipo + '!\n')
    elif opcao == '4':
        print('Vamos pesquisar um ' + opcao_tipo + '!\n')

# NÃO ENCONTROU ITEM
def printar_nao_encontrou_cpf(cpf):
    printar_cor('\nCPF: ' + cpf + ' não consta na lista dos cpf de clientes...', RED)

def printar_nao_encontrou_prod(prod):
    printar_cor('\nProduto: ' + prod + ' não consta na lista de produtos...', RED)


# VALORES ATUAIS
def printar_valores_atuais_clientes(nome, num, email, end):
    print('===== VALORES ATUAIS =====')
    print('1. NOME: ' + nome)
    print('2. NUMERO: ' + num)
    print('3. EMAIL: ' + email)
    print('4. ENDEREÇO: ' + end)
    printar_cor('5. CANCELAR EDIÇÃO', RED)

def printar_valores_atuais_produtos(produto, qntd, preco, desc):
    print('===== VALORES ATUAIS =====')
    print('1. Nome: ' + produto)
    print('2. Quantidade: ' + str(qntd))
    print('3. Preço: ' + '{:.2f}'.format(preco))
    print('4. Descrição: ' + desc)
    print('5. CANCELAR EDIÇÃO')


# LISTAS
def printar_lista_produtos():
    if len(bd.produtos) == 0:
        print('\nLista de produtos está vazia')
        return

    print('LISTA DE PRODUTOS:\n')
    # printa cada produto
    for prod in bd.produtos.keys():
        printar_produto(prod)
        print()

def printar_lista_clientes():
    if len(bd.clientes) == 0:
        print('\nLista de clientes está vazia')
        return

    print('LISTA DE CLIENTES:\n')
    # printa cada cliente
    for cpf in bd.clientes.keys():
        printar_cliente(cpf)
        print()

def printar_lista_vendas():
    if len(bd.vendas) == 0:
        print('\nLista de vendas está vazia')
        return

    print('LISTA DE VENDAS:\n')
    # printa cada cliente
    for i in range(len(bd.vendas)):
        printar_venda(i)
        print()


# PRINT DE CLIENTE, PRODUTO E PEDIDO
def printar_cliente(cpf):
    print('Cliente: ' + bd.clientes[cpf]['nome'])
    print('Cpf: ' + mask_cpf(cpf))
    print('Número: ' + bd.clientes[cpf]['num'])
    print('Email: ' + bd.clientes[cpf]['email'])
    print('Endereço: ' + bd.clientes[cpf]['end'])

def printar_produto(prod):
    print('Produto: ' + prod)
    print('Quantidade em estoque: ' + str(bd.produtos[prod]['qntd']))
    print('Preço: R$ ' + '{:.2f}'.format(bd.produtos[prod]['preco']))
    print('Descrição : ' + bd.produtos[prod]['desc'])

def printar_venda(ID):
    venda = bd.vendas[ID]
    print('===== ID: ' + str(ID) + ' =====')
    print('CPF do cliente: ' + mask_cpf(venda['cpf']))
    print('PRODUTOS SELECIONADOS:')
    printar_produtos_selecionados_e_total(venda['produtos_qntd_preco'])

def printar_produtos_selecionados_e_total(produtos_qntd_preco):
    # imprime cada produto do pedido, seu preço e quantidade
    total = 0
    for prod in produtos_qntd_preco.keys():

        qntd = int(produtos_qntd_preco[prod]['qntd'])
        preco = float(produtos_qntd_preco[prod]['preco'])
        total_prod = preco * qntd

        print(qntd, prod,'por', 'R$ {:.2f}'.format(preco), '=> R$', '{:.2f}'.format(total_prod))
        total += total_prod

    print('\nCusto total: ' + '{:.2f}'.format(total))


def mask_cpf(cpf):
    return cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]

def pegar_opcao():
    opcao = input(BLUE + 'Opção: ' + RESET)
    print()
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
        printar_cor('Voltando ao menu...', RED)
        return None
    else:
        return opcao

def printar_item_adicionado(item_tipo, item_nome):
    printar_cor('\n' + item_tipo + ' ' + item_nome + ' adicionado!', GREEN)


