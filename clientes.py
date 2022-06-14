import database as bd
import interacoes

def start():
    interacoes.printar_opcoes('cliente')

    opcao = interacoes.pegar_opcao()
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
        return

    if opcao == '5':
        interacoes.printar_lista_clientes()
        return

    interacoes.printar_acao(opcao, 'cliente')
    cpf = input('CPF do cliente: ')

    if validar_cpf(cpf) is not True:
        return

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
    if cpf in bd.clientes.keys():
        opcao = input('Esse cliente ja esta cadastrado, deseja edita-lo (s/n): ')
        if opcao == 's':
            editar(cpf)
            return
        else:
            return

    # pegar dados do cliente
    nome = input('Nome do cliente: ')
    num = input('Número de telefone: ')
    while True:
        email = input('Email: ')
        if validar_email(email):
            break
        else:
            print('Email inválido tente novamente...\n')
            continue
    end = input('Endereço: ')

    bd.clientes[cpf] = {
        'nome': nome,
        'num' : num,
        'email' : email,
        'end' : end
    }

    interacoes.printar_item_adicionado('Cliente ', nome + ' de CPF: ' + interacoes.mask_cpf(cpf))

def remover(cpf):
    if cpf not in bd.clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        interacoes.printar_cliente(cpf)
        opcao = input('\nDeseja remover ' + bd.clientes[cpf]['nome'] + ' (s/n)? ')
        if opcao == 's':
            print('\nCliente removido com sucesso!')
            bd.clientes.pop(cpf)
        else:
            print('Cliente não foi removido.')
            return


def editar(cpf):
    if cpf not in bd.clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        # pega valores atuais
        nome = bd.clientes[cpf]['nome']
        num  = bd.clientes[cpf]['num']
        email = bd.clientes[cpf]['email']
        end  = bd.clientes[cpf]['end']

        while True:
            interacoes.printar_valores_atuais_clientes(nome, num, email, end)

            opcao = input('\nO que deseja editar? ')

            if opcao == '1':
                nome = input('Novo nome: ')
            elif opcao == '2':
                num = input('Novo número de telefone: ')
            elif opcao == '3':
                email = input('Novo email: ')
            elif opcao == '4':
                end = input('Novo endereço: ')
            elif opcao == '5':
                break

            # atualiza cliente
            bd.clientes[cpf] = { 'nome': nome, 'num' : num, 'email' : email, 'end' : end }

            opcao = input('Deseja continuar editando (s/n)? ')
            if opcao == 's':
                continue
            else:
                break

def pesquisar(cpf):
    if cpf not in bd.clientes.keys():
        interacoes.printar_nao_encontrou_cpf(cpf)
    else:
        interacoes.printar_cliente(cpf)

def validar_cpf(cpf):
    if len(cpf) != 11:
        print('\nCPF inválido')
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
        return True
    else:
        print('\nCPF Inválido')
        return False

# se possuir um arroba e não for o primeiro caractere é válido.
def validar_email(email):
    arroba_contar = 0

    for c in email:
        if c == '@' and c != email[0:1]:
            arroba_contar += 1

    if arroba_contar == 1:
        return True
    else:
        return False