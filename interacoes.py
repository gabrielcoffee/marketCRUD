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