
from datetime import datetime


def confirmar_opcao():

    choice = str(input('\nDeseja iniciar novo cadastro? [SIM/NAO]: ')).strip().lower()

    while choice != 'sim' and choice != 'nao':
        print('Escolha invalida. Digite sim ou nao.')
        choice = str(input('\nDeseja iniciar novo cadastro? [SIM/NAO]: ')).strip().lower()

    return choice


def escolha_busca_cliente():
    try:
        print('\n==Consulta de clientes==\n')
        print('1 - Procurar por cpf')
        print('2 - Procurar por nome')
        print('3 - Voltar para o menu anterior')

        escolha = int(input('Escolha uma opcao: '))
        return escolha

    except ValueError:
        print('\nVoce precisa digitar um numero correspondente as opcoes. Tente novamente.')


def escolha_busca_livro():
    try:
        print('\n==Verificar livro==\n')
        print('1 - Procurar por nome')
        print('2 - Procurar por ano')
        print('3 - Procurar por autor')
        print('4 - Voltar para o menu anterior')

        escolha = int(input('Escolha uma opcao: '))
        return escolha

    except ValueError:
        print('\nVoce precisa digitar um numero correspondente as opcoes. Tente novamente.')


def validar_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
    
    if cpf == cpf[0] * 11:
        return False

    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0


    if resto != int(cpf[9]):
        return False

    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True


def validar_data():

    while True:
        data = str(input('Digite a data colocando as barras. (DD/MM/AA): ')).strip()

        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            break

        except ValueError:
            print('\nData invalida! Use o formato DD/MM/AA')

    return data
