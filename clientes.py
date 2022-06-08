from database import clientes
import interacoes

def start():
    interacoes.printar_opcoes('clientes')

    opcao = interacoes.pegar_opcao()
    if opcao is None:
        return

    cpf = input('CPF do cliente: ')

    if validar_cpf(cpf):
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
    if cpf in clientes.keys():
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

    clientes[cpf] = {
        'nome': nome,
        'num' : num,
        'end' : end
    }

    interacoes.printar_item_adicionado('Cliente', nome + ' de CPF: ' + cpf)

def remover(cpf):
    if cpf not in clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        clientes.pop(cpf)

def editar(cpf):
    if cpf not in clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        # pega valores atuais
        nome = clientes[cpf]['nome']
        num  = clientes[cpf]['num']
        end  = clientes[cpf]['end']

        while True:
            print('===== VALORES ATUAIS =====')
            print('1. NOME: ' + nome)
            print('2. NUMERO: ' + num)
            print('3. ENDEREÇO: ' + end)
            print('4. CANCELAR EDIÇÃO')

            opcao = input('\nO que deseja editar? ')

            if opcao == '1':
                nome = input('Novo nome: ')
            elif opcao == '2':
                num = input('Novo número de telefone: ')
            elif opcao == '3':
                end = input('Novo endereço: ')
            elif opcao == '4':
                break

            # atualiza cliente
            clientes[cpf] = { 'nome': nome, 'num' : num, 'end' : end }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 'n':
                break
            elif opcao == 's':
                continue

def pesquisar(cpf):
    if cpf not in clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        cliente = clientes[cpf]
        print('\nNome: ' + cliente['nome'])
        print('Número: ' + cliente['num'])
        print('Endereço: ' + cliente['end'])

def validar_cpf(cpf):
    if len(cpf) != 11:
        print('\nCPF inválido\n')
        return False

    digitos = []
    for d in cpf:
        digitos.append(int(d))

    # PRIMEIRO DIGITO DE VERIFICAÇÃO
    soma = (digitos[0] * 10) + (digitos[1] * 9) + (digitos[2] * 8) \
            + (digitos[3] * 7) + (digitos[4] * 6) + (digitos[5] * 5) \
            + (digitos[6] * 4) + (digitos[7] * 3) + (digitos[8] * 2)

    resto = soma % 11
    verif1 = 11 - resto
    if verif1 >= 10:
        verif1 = 0

    # SEGUNDO DIGITO DE VERIFICAÇÃO
    soma = (digitos[0] * 11) + (digitos[1] * 10) + (digitos[2] * 9) \
            + (digitos[3] * 8) + (digitos[4] * 7) + (digitos[5] * 6) \
            + (digitos[6] * 5) + (digitos[7] * 4) + (digitos[8] * 3) + digitos[9] * 2

    resto = soma % 11
    verif2 = 11 - resto
    if verif2 >= 10:
        verif2 = 0

    if verif1 == digitos[9] and verif2 == digitos[10]:
        print('\nCPF Válido\n')
        return True
    else:
        print('\nCPF Inválido')
        return False