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
    printar_cor('========================', GREEN)
    printar_cor('Grupo: OS TRAVA PYTHON', BLUE)
    printar_cor('Alunos: ', GREEN)
    print('   Angelo Sequinel,\n   Lohan Berg,\n   Leonardo Cavalli,\n   Gabriel Fernandes.')
    printar_cor('Sistema para mercado', BLUE)
    printar_cor('========================', GREEN)

def printar_menu():
    printar_cor('\n======= MENU =======', GREEN)
    print_opcao(1, 'Clientes')
    print_opcao(2, 'Produtos')
    print_opcao(3, 'Compra e Venda')
    print_opcao(4, 'Fechar programa')

def print_opcao(num, string):
    print(BLUE + '['+str(num)+'] ' + RESET + string)

def printar_opcoes(opcao_tipo):
    print_opcao(1, 'Adicionar ' + opcao_tipo)
    print_opcao(2, 'Remover ' + opcao_tipo)
    print_opcao(3, 'Editar ' + opcao_tipo)
    print_opcao(4, 'Pesquisar ' + opcao_tipo)
    print_opcao(5, 'Lista de ' + opcao_tipo + 's')
    printar_cor('Enter: Voltar ao menu\n', RED)

def printar_opcoes_compras():
    print_opcao(1, 'Gerar compra')
    print_opcao(2, 'Listar vendas')
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
    printar_cor('====== VALORES ATUAIS ======', GREEN)
    print_opcao(1, 'NOME: ' + nome)
    print_opcao(2, 'NUMERO: ' + num)
    print_opcao(3, 'EMAIL: ' + email)
    print_opcao(4, 'ENDEREÇO: ' + end)
    printar_cor('[5] CANCELAR EDIÇÃO', RED)

def printar_valores_atuais_produtos(produto, qntd, preco, desc):
    printar_cor('====== VALORES ATUAIS ======', GREEN)
    print_opcao(1, 'Nome: ' + produto)
    print_opcao(2, 'Quantidade: ' + str(qntd))
    print_opcao(3, 'Preço: ' + '{:.2f}'.format(preco))
    print_opcao(4, 'Descrição: ' + desc)
    printar_cor('[5] CANCELAR EDIÇÃO', RED)


# LISTAS
def printar_lista_produtos():
    if len(bd.produtos) == 0:
        printar_cor('\nLista de produtos está vazia', RED)
        return

    printar_cor('LISTA DE PRODUTOS:', GREEN)
    # printa cada produto
    for prod in bd.produtos.keys():
        printar_produto(prod)


def printar_lista_clientes():
    if len(bd.clientes) == 0:
        printar_cor('\nLista de clientes está vazia', RED)
        return

    printar_cor('LISTA DE CLIENTES:', GREEN)
    # printa cada cliente
    for cpf in bd.clientes.keys():
        printar_cliente(cpf)

def printar_lista_vendas():
    if len(bd.vendas) == 0:
        printar_cor('\nLista de vendas está vazia', RED)
        return

    printar_cor('LISTA DE VENDAS:\n', GREEN)
    # printa cada cliente
    for i in range(len(bd.vendas)):
        printar_venda(i)


# PRINT DE CLIENTE, PRODUTO E PEDIDO
def printar_cliente(cpf):
    print()
    printar_cor('Cliente: ' + bd.clientes[cpf]['nome'], BLUE)
    print('Cpf: ' + mask_cpf(cpf))
    print('Número: ' + bd.clientes[cpf]['num'])
    print('Email: ' + bd.clientes[cpf]['email'])
    print('Endereço: ' + bd.clientes[cpf]['end'])

def printar_produto(prod):
    print()
    printar_cor('Produto: ' + prod, BLUE)
    print('Quantidade em estoque: ' + str(bd.produtos[prod]['qntd']))
    print('Preço: R$ ' + '{:.2f}'.format(bd.produtos[prod]['preco']))
    print('Descrição : ' + bd.produtos[prod]['desc'])

def printar_venda(ID):
    print()
    venda = bd.vendas[ID]
    printar_cor('============= ID: ' + str(ID) + ' =============', BLUE)
    print('CPF do cliente: ' + mask_cpf(venda['cpf']))
    printar_cor('< PRODUTOS SELECIONADOS >', GREEN)
    printar_produtos_selecionados_e_total(venda['produtos_qntd_preco'])

def printar_produtos_selecionados_e_total(produtos_qntd_preco):
    # imprime cada produto do pedido, seu preço e quantidade
    total = 0
    for prod in produtos_qntd_preco.keys():

        qntd = int(produtos_qntd_preco[prod]['qntd'])
        preco = float(produtos_qntd_preco[prod]['preco'])
        total_prod = preco * qntd

        print(qntd, prod,'por', '{:.2f' '}'.format(preco), '-->', text_preco(total_prod))
        total += total_prod

    print('CUSTO TOTAL --> ' + text_preco(total))

def text_preco(preco):
    return GREEN + 'R$ ' + '{:.2f}'.format(preco) + RESET

def mask_cpf(cpf):
    return cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]

def pegar_opcao():
    opcao = input(RED + '--> ' + RESET)
    print()
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
        printar_cor('Voltando ao menu...', RED)
        return None
    else:
        return opcao

def printar_item_adicionado(item_tipo, item_nome):
    printar_cor('\n' + item_tipo + ' ' + item_nome + ' adicionado!', GREEN)


