from Projeto import conexao_bd
from Projeto.conexao_bd import conectar
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

    # Remove tudo que não for número.
    # Exemplo:
    # "123.456.789-09" -> "12345678909"
    cpf = ''.join(filter(str.isdigit, cpf))

    # Um CPF precisa ter exatamente 11 números.
    if len(cpf) != 11:
        return False

    # Verifica se todos os números são iguais.
    # Exemplos:
    # "11111111111"
    # "22222222222"
    # "00000000000"
    #
    # Esses CPFs possuem 11 caracteres, mas são inválidos.
    if cpf == cpf[0] * 11:
        return False

    # ==========================================================
    # CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR
    # ==========================================================

    # Vamos somar os 9 primeiros números do CPF,
    # cada um multiplicado por um peso diferente.
    #
    # Exemplo:
    # CPF: 12345678909
    #
    # 1 x 10
    # 2 x 9
    # 3 x 8
    # 4 x 7
    # 5 x 6
    # 6 x 5
    # 7 x 4
    # 8 x 3
    # 9 x 2

    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    # Depois de fazer a soma, multiplicamos por 10
    # e pegamos o resto da divisão por 11.
    resto = (soma * 10) % 11

    # Se o resultado for 10, o dígito verificador será 0.
    if resto == 10:
        resto = 0

    # O primeiro dígito verificador está na posição 9.
    #
    # Exemplo:
    # 123456789-0 9
    #          ^
    #       primeiro
    #       dígito
    #
    # Se o resultado calculado for diferente do CPF,
    # significa que o CPF é inválido.
    if resto != int(cpf[9]):
        return False

    # ==========================================================
    # CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR
    # ==========================================================

    # Agora utilizamos os 10 primeiros números,
    # incluindo o primeiro dígito verificador que acabamos
    # de validar.
    #
    # Os pesos agora vão de 11 até 2.
    #
    # Exemplo:
    # 1 x 11
    # 2 x 10
    # 3 x 9
    # 4 x 8
    # 5 x 7
    # 6 x 6
    # 7 x 5
    # 8 x 4
    # 9 x 3
    # 0 x 2

    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    # Novamente fazemos o cálculo do resto.
    resto = (soma * 10) % 11

    # Se o resultado for 10, transformamos em 0.
    if resto == 10:
        resto = 0

    # O segundo dígito verificador está na posição 10.
    #
    # Exemplo:
    # 123456789-09
    #            ^
    #         segundo
    #         dígito
    if resto != int(cpf[10]):
        return False

    # Se chegou até aqui, todas as validações passaram.
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

def teste(self):

    cursor = self.conexao_bd.cursor()

    livros = cursor.fetchall()

    cursor.execute("""
                                SELECT
                                    CPF_CLIENTE,
                                    CODIGO_LIVRO,
                                    QUANTIDADE_EMPRESTADA
                                FROM EMPRESTIMO
                                WHERE CODIGO_LIVRO = %s
                                """, (livros[0][1],))

    emprestados = cursor.fetchall()

    if emprestados:

        for emprestado in emprestados:
            cursor.execute("""
                                        SELECT
                                            NOME,
                                            CPF,
                                            TELEFONE
                                        FROM CLIENTES
                                        WHERE CPF = %s
                                    """, (emprestado[0],))

            clientes = cursor.fetchone()

            print(f'CLIENTE: {clientes[0]}, '
                  f'CPF: {clientes[1]}, '
                  f'TELEFONE: {clientes[2]}, '
                  f'Em posse de {emprestado[2]} desse livro\n')


    else:
        print('\nNenhum empréstimo foi encontrado para este livro!')
