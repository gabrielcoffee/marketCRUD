def printar_inicio():
    print('===========================================')
    print('Grupo: Os trava python')
    print('Alunos: Angelo, Lohan, Leonardo, Gabriel F.')
    print('Sistema de clientes e produtos')
    print('===========================================')

def printar_menu():
    print('\n===== MENU =====')
    print('1. Clientes')
    print('2. Listar clientes')
    print('3. Produtos')
    print('4. Listar produtos')
    print('5. Salvar e SAIR')

def printar_opcoes(opcao_tipo):
    print('\n1. Adicionar ' + opcao_tipo)
    print('2. Remover ' + opcao_tipo)
    print('3. Editar ' + opcao_tipo)
    print('4. Pesquisar ' + opcao_tipo)

def printar_nao_encontrou_cpf(cpf):
    print('\nCPF ' + cpf + ' não consta na lista dos cpf de clientes...\n')

def printar_nao_encontrou_prod(prod):
    print('\nProduto ' + prod + ' não consta na lista de produtos...\n')

def printar_dict(dict, lista_tipo):
    if len(dict) == 0:
        print('\nLista de ' + lista_tipo + ' está vazia')
        return

    print('LISTA DE ' + lista_tipo.upper() + ':\n')
    if lista_tipo == 'clientes':
        for cpf in dict.keys():
            print('cliente: ' + dict[cpf]['nome'])
            print('cpf: ' + cpf)
            print('número: ' + dict[cpf]['num'])
            print('endereço: ' + dict[cpf]['end'])

    elif lista_tipo == 'produtos':
        for prod in dict.keys():
            print()
            print('produto: ' + prod)
            print('preço: ' + dict[prod]['preco'])
            print('descrição : ' + dict[prod]['desc'])

def pegar_opcao():
    opcao = input('Opção: ')
    if opcao == '':
        print('Nenhuma opção selecionada, voltando ao menu')
        return None
    else:
        return opcao

def printar_item_adicionado(item_tipo, item_nome):
    print(item_tipo + ' "' + item_nome + '" adicionado!')
