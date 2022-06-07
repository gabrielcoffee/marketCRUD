from main import clientes_bd
from interacoes import printar_opcoes, printar_nao_encontrou_cpf

def start():
    printar_opcoes('clientes')

    opcao = input('Opção: ')
    cpf = input('CPF do cliente: ')

    if opcao == '1':
        adicionar(cpf)
    elif opcao == '2':
        remover(cpf)
    elif opcao == '3':
        editar(cpf)
    elif opcao == '4':
        pesquisar(cpf)

def adicionar(cpf):
        
    # se cpf ja estiver no dicionario...
    if cpf in clientes_bd.keys():
        opcao = input('Esse cliente ja esta cadastrado, deseja edita-lo (s/n): ')
        if opcao == 's':
            editar(cpf)
            return
        else:
            return

    # se cpf não estiver no dicionario...
    nome = input('Nome do cliente: ')
    num = input('Número de telefone do cliente: ')
    end = input('Endereço do cliente: ')

    clientes_bd[cpf] = {
        'nome': nome,
        'num' : num,
        'end' : end
    }

def remover(cpf):
    if cpf not in clientes_bd.keys():
        printar_nao_encontrou_cpf(cpf)
    else:
        clientes_bd.pop(cpf)

def editar(cpf):
    if cpf not in clientes_bd.keys():
        printar_nao_encontrou_cpf(cpf)
    else:
        # pega valores atuais
        nome = clientes_bd[cpf]['nome']
        num  = clientes_bd[cpf]['num']
        end  = clientes_bd[cpf]['end']

        while True:
            print('===== VALORES ATUAIS =====')
            print('1. NOME: ' + nome)
            print('2. NUMERO: ' + num)
            print('3. ENDEREÇO: ' + end)
            print('4. CANCELAR EDIÇÃO')

            opcao = input('\nO que deseja editar? ')

            if opcao == 1:
                nome = input('Novo nome: ')
            elif opcao == 2:
                num = input('Novo número de telefone: ')
            elif opcao == 3:
                end = input('Novo endereço: ')
            elif opcao == 4:
                break

            # atualiza cliente
            clientes_bd[cpf] = { 'nome': nome, 'num' : num, 'end' : end }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 'n':
                break
            elif opcao == 's':
                continue

def pesquisar(cpf):
    if cpf not in clientes_bd.keys():
        printar_nao_encontrou_cpf(cpf)
    else:
        cliente = clientes_bd[cpf]
        print('\nNome: ' + cliente['nome'])
        print('Número: ' + cliente['num'])
        print('Endereço: ' + cliente['end'])

def printar_lista():
    if len(clientes_bd) == 0:
        print('\nLista de clientes está vazia\n')
        return

    print('LISTA DE CLIENTES:\n')
    for cpf in clientes_bd.keys():
        print()
        print('cliente: ' + clientes_bd[cpf]['nome'])
        print('cpf: ' + cpf)
        print('número: ' + clientes_bd[cpf]['num'])
        print('endereço: ' + clientes_bd[cpf]['end'])