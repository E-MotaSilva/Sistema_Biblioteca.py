from Projeto.conexao_bd import conectar
from Projeto.funcoes_uteis import confirmar_opcao, escolha_busca_cliente, escolha_busca_livro, validar_cpf, validar_data

class Biblioteca:

    def __init__(self):
        self.conexao_bd = conectar()
        self.livros = []
        self.clientes = []


    def cadastrar_livro(self):

        print('\n==Cadastrar livro==')

        choice = confirmar_opcao()

        if choice == 'sim':
            while True:

                print('\n==Cadastrar livro==\n')

                nome = str(input('Nome do livro: ')).strip().upper()
                autor = str(input('Autor: ')).strip().upper()
                data_lancamento = validar_data()
                codigo_livro = int(input('Digite o código do livro: '))

                if not all([nome, autor, data_lancamento, codigo_livro]):
                    print('Voce deixou algum campo em branco. Por favor verifique e refaça o cadastro.')
                    break

                while True:
                    try:
                        quantidade = int(input('Quantidade disponivel: '))

                        if quantidade <= 0:
                            print('A quantidade não pode ser negativa!')
                        else:
                            break

                    except ValueError:
                        print('Opcao invalida. Digite um numero.')

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT codigo_id
                        FROM LIVROS
                        WHERE nome = %s
                        AND autor = %s
                    """, (nome, autor))

                    livro_encontrado = cursor.fetchone()

                    if livro_encontrado:

                        print('Este LIVRO ja esta no catalogo!')

                    else:

                        cursor.execute("""
                            INSERT INTO LIVROS
                            (
                                codigo_id,
                                nome,
                                autor,
                                data_lancamento,
                                quantidade_cadastrada,
                                quantidade_disponivel
                            )
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """, (
                            codigo_livro,
                            nome,
                            autor,
                            data_lancamento,
                            quantidade,
                            quantidade
                        ))

                        self.conexao_bd.commit()

                        print('LIVRO cadastrado com sucesso!')

                except Exception as erro:

                    self.conexao_bd.rollback()

                    print(f'Erro ao cadastrar livro: {erro}')

                finally:

                    cursor.close()

                choice = confirmar_opcao()

                if choice == 'nao':
                    print('Retornando para o menu anterior...!')
                    break


    def cadastrar_cliente(self):

        print('\n==Cadastrar cliente==')

        choice = confirmar_opcao()

        if choice == 'sim':

            while True:

                print('\n==Cadastrar cliente==\n')

                nome = str(input('Nome: ')).strip().upper()

                data_nascimento = validar_data()

                while True:
                    cpf = str(input('CPF: ')).strip()

                    if validar_cpf(cpf):
                        break

                    print('\nCPF inválido! Digite novamente.')

                telefone = str(input('Telefone: ')).strip()
                email = str(input('Email: ')).strip().upper()

                if not all([nome, data_nascimento, cpf, telefone]):
                    print('Voce deixou campos em branco. Por favor verifique e refaça o cadastro.')
                    break

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT cpf
                        FROM CLIENTES
                        WHERE cpf = %s """, (cpf,))

                    cliente_encontrado = cursor.fetchone()

                    if cliente_encontrado:
                        print('Este CPF já está vinculado a um cliente!')

                    else:
                        cursor.execute("""
                            INSERT INTO CLIENTES
                            (cpf, nome, data_nascimento, telefone, email)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (cpf, nome, data_nascimento, telefone, email,))

                        self.conexao_bd.commit()

                        print('\nCliente cadastrado com sucesso!')

                except Exception as erro:

                    self.conexao_bd.rollback()
                    print(f'Erro ao cadastrar cliente: {erro}')

                finally:

                    cursor.close()

                choice = confirmar_opcao()

                if choice == 'nao':
                    print('Retornando para o menu anterior...!')
                    break


    def consulta_cliente(self):

        escolha = escolha_busca_cliente()

        while escolha != 3:

            if escolha == 1:

                cpf = str(input('Digite o CPF: ')).strip()

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT
                            cpf,
                            nome,
                            data_nascimento,
                            telefone,
                            email
                        FROM CLIENTES
                        WHERE cpf = %s
                    """, (cpf,))
                    
                    cliente = cursor.fetchone()

                    if cliente:

                        print()
                        print('-' * 30)
                        print(f'CPF: {cliente[0]}')
                        print(f'NOME: {cliente[1]}')
                        print(f'DATA: {cliente[2]}')
                        print(f'TELEFONE: {cliente[3]}')
                        print(f'EMAIL: {cliente[4]}')
                        print('-' * 30)

                    else:

                        print('\nCliente nao encontrado!')

                except Exception as erro:

                    print(f'\nErro ao consultar cliente: {erro}')

                finally:

                    cursor.close()

            elif escolha == 2:

                nome = str(input('Digite o nome: ')).strip().upper()

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT
                            cpf,
                            nome,
                            data_nascimento,
                            telefone,
                            email
                        FROM CLIENTES
                        WHERE nome = %s
                    """, (nome,))

                    clientes = cursor.fetchall()

                    if clientes:

                        for cliente in clientes:
                            print()
                            print('-' * 30)
                            print(f'CPF: {cliente[0]}')
                            print(f'NOME: {cliente[1]}')
                            print(f'DATA: {cliente[2]}')
                            print(f'TELEFONE: {cliente[3]}')
                            print(f'EMAIL: {cliente[4]}')
                            print('-' * 30)

                    else:

                        print('\nCliente nao encontrado!')

                except Exception as erro:

                    print(f'\nErro ao consultar cliente: {erro}')

                finally:

                    cursor.close()

            elif escolha == 3:

                print('Voltando para o menu anterior...!')

            else:

                print('Opcao invalida.')

            escolha = escolha_busca_cliente()


    def consulta_livro(self):

        escolha = escolha_busca_livro()

        while escolha != 4:

            if escolha == 1:
                nome = str(input('Digite o nome: ')).strip().upper()

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT
                            NOME,
                            CODIGO_ID,
                            AUTOR,
                            DATA_LANCAMENTO,
                            QUANTIDADE_CADASTRADA,
                            QUANTIDADE_DISPONIVEL
                        FROM LIVROS
                        WHERE NOME = %s
                    """, (nome,))

                    livros = cursor.fetchall()

                    if livros:

                        print()
                        print('-' * 30)
                        print(f'CODIGO: {livros[0][1]}')
                        print(f'AUTOR: {livros[0][2]}')
                        print(f'DATA LANCAMENTO: {livros[0][3]}')
                        print(f'QUANTIDADE CADASTRADA: {livros[0][4]}')
                        print(f'QUANTIDADE DISPONIVEL: {livros[0][5]}')
                        print('-' * 30)

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

                    else:
                        print('\nLivro nao encontrado!')

                except Exception as erro:
                    print(f'\nErro ao consultar Livros: {erro}')

                finally:
                    cursor.close()

            elif escolha == 2:
                lancamento = str(input('Digite a data de lançamento. Coloque as barras(DD/MM/AAAA): ')).strip().upper()

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT
                            NOME,
                            CODIGO_ID,
                            AUTOR,
                            DATA_LANCAMENTO,
                            QUANTIDADE_CADASTRADA,
                            QUANTIDADE_DISPONIVEL
                        FROM LIVROS
                        WHERE DATA_LANCAMENTO = %s
                    """, (lancamento,))

                    livros = cursor.fetchall()

                    if livros:

                        for livro in livros:

                            print()
                            print('-' * 30)
                            print(f'NOME: {livro[0]}')
                            print(f'CODIGO: {livro[1]}')
                            print(f'AUTOR: {livro[2]}')
                            print(f'QUANTIDADE CADASTRADA: {livro[4]}')
                            print(f'QUANTIDADE DISPONIVEL: {livro[5]}')
                            print('-' * 30)

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
                        print('\nLivro nao encontrado!')

                except Exception as erro:
                    print(f'\nErro ao consultar Livros: {erro}')

                finally:
                    cursor.close()

            elif escolha == 3:
                autor = str(input('Digite o nome do autor: ')).strip().upper()

                cursor = self.conexao_bd.cursor()

                try:

                    cursor.execute("""
                        SELECT
                            NOME,
                            CODIGO_ID,
                            AUTOR,
                            DATA_LANCAMENTO,
                            QUANTIDADE_CADASTRADA,
                            QUANTIDADE_DISPONIVEL
                        FROM LIVROS
                        WHERE AUTOR = %s
                    """, (autor,))

                    livros = cursor.fetchall()

                    if livros:

                        for livro in livros:

                            print()
                            print('-' * 30)
                            print(f'NOME: {livro[0]}')
                            print(f'CODIGO: {livro[1]}')
                            print(f'DATA LANCAMENTO: {livro[3]}')
                            print(f'QUANTIDADE CADASTRADA: {livro[4]}')
                            print(f'QUANTIDADE DISPONIVEL: {livro[5]}')
                            print('-' * 30)

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
                        print('\nLivro nao encontrado!')

                except Exception as erro:
                    print(f'\nErro ao consultar Livros: {erro}')

                finally:
                    cursor.close()

            elif escolha == 4:
                print('\nVoltando para o menu anterior...')

            else:
                print('\nOpção invalida!')

            escolha = escolha_busca_livro()


    def emprestar_livro(self):

        print('\n==Emprestar livro==\n')

        destino = str(input('Digite o CPF do CLIENTE: '))

        cursor = self.conexao_bd.cursor()


        try:

            cursor.execute("""
                SELECT
                    CPF
                FROM CLIENTES
                WHERE cpf = %s
            """, (destino,))

            clientes = cursor.fetchall()

            if clientes:

                escolha = str(input('Digite o livro que o cliente deseja: ')).strip().upper()
                quantidade = int(input('Quantos livros deseja?: '))

                confirmacao = str(input('Deseja confirmar a operaçãao?: ')).strip().upper()

                if confirmacao == 'SIM':

                    cursor.execute("""
                        SELECT
                            CODIGO_ID,
                            NOME,
                            QUANTIDADE_DISPONIVEL
                        FROM LIVROS
                        WHERE NOME = %s AND QUANTIDADE_DISPONIVEL >= %s
                    """, (escolha, quantidade))

                    livros = cursor.fetchall()

                    if livros:

                        cursor.execute("""
                            UPDATE LIVROS
                            SET QUANTIDADE_DISPONIVEL = QUANTIDADE_DISPONIVEL - %s
                            WHERE NOME = %s AND QUANTIDADE_DISPONIVEL >= %s
                        """, (quantidade, escolha, quantidade))

                        if cursor.rowcount == 1:

                            cursor.execute("""
                                INSERT INTO EMPRESTIMO (
                                    CPF_CLIENTE,
                                    CODIGO_LIVRO,
                                    QUANTIDADE_EMPRESTADA
                                )
                                VALUES(%s, %s, %s)
                                """, (destino,livros[0][0], quantidade))

                            self.conexao_bd.commit()
                            print('Operação realizada com sucesso!')

                        else:
                            self.conexao_bd.rollback()
                            print('Não foi possível completar a operação')

                    else:
                        print('\nLivro não encontrado!')

                elif confirmacao == 'NAO':

                    self.conexao_bd.rollback()

                else:
                    self.conexao_bd.rollback()
                    print('Opção invalida!')

            else:
                print('\nCliente nao encontrado!')

        except Exception as erro:
            print(f'\nErro ao consultar Livros: {erro}')

        finally:
            cursor.close()


    def devolver_livro(self):

            print('\n== Devolver livro ==\n')

            cliente_devolucao = str(input('Digite o CPF do CLIENTE que fará a devolução: '))

            cursor = self.conexao_bd.cursor()

            try:
                cursor.execute("""
                    SELECT
                        CPF_CLIENTE,
                        ID_EMPRESTIMO,
                        QUANTIDADE_EMPRESTADA,
                        CODIGO_LIVRO
                    FROM EMPRESTIMO
                    WHERE CPF_CLIENTE = %s AND QUANTIDADE_EMPRESTADA > 0
                """, (cliente_devolucao,))

                devolucoes = cursor.fetchall()

                if devolucoes:

                    livro = str(input('Digite o nome do livro que deseja devolver: ')).upper().strip()

                    cursor.execute("""
                        SELECT
                            LIVROS.NOME,
                            LIVROS.CODIGO_ID,
                            EMPRESTIMO.ID_EMPRESTIMO,
                            EMPRESTIMO.QUANTIDADE_EMPRESTADA
                        FROM LIVROS
                        INNER JOIN EMPRESTIMO
                            ON EMPRESTIMO.CODIGO_LIVRO = LIVROS.CODIGO_ID
                        WHERE LIVROS.NOME = %s AND EMPRESTIMO.CPF_CLIENTE = %s AND EMPRESTIMO.QUANTIDADE_EMPRESTADA > 0
                    """, (livro, cliente_devolucao))

                    dev_livros = cursor.fetchall()

                    if dev_livros:

                        quantidade_emprestada = dev_livros[0][3]

                        quantidade = int(input('Quantidade a ser devolvida: '))

                        if quantidade <= 0:
                            print('A quantidade deve ser maior que zero!')

                        elif quantidade > quantidade_emprestada:
                            print('Erro: a quantidade informada é maior que a quantidade emprestada.')

                        else:
                            cursor.execute("""
                                UPDATE EMPRESTIMO
                                SET QUANTIDADE_EMPRESTADA = QUANTIDADE_EMPRESTADA - %s
                                WHERE ID_EMPRESTIMO = %s AND CPF_CLIENTE = %s AND QUANTIDADE_EMPRESTADA >= %s
                            """, (quantidade, dev_livros[0][2], cliente_devolucao, quantidade))

                            cursor.execute("""
                                UPDATE LIVROS
                                SET QUANTIDADE_DISPONIVEL = QUANTIDADE_DISPONIVEL + %s
                            """, (quantidade,))

                            cursor.execute("""
                                DELETE FROM EMPRESTIMO
                                WHERE QUANTIDADE_EMPRESTADA = 0
                            """)

                            if cursor.rowcount > 0:

                                self.conexao_bd.commit()
                                print('\nDevolução realizada com sucesso!')

                            else:
                                self.conexao_bd.rollback()
                                print('Não foi possível realizar a devolução')

                    else:
                        print('\nEsse cliente não possui empréstimo ativo')

                else:
                    print('\nEsse cliente não possui livros pendentes de devolução')
            except Exception as erro:
                self.conexao_bd.rollback()
                print(f'\nErro ao consultar Livros: {erro}')

            finally:
                cursor.close()


    def remover_livro(self):

        print('\n== Remover livro ==\n')

        opcao = str(
            input('Digite o nome do livro que deseja excluir do catálogo: ')
        ).strip().upper()

        cursor = self.conexao_bd.cursor()

        try:
            cursor.execute("""
                SELECT
                    NOME,
                    CODIGO_ID,
                    AUTOR,
                    DATA_LANCAMENTO,
                    QUANTIDADE_CADASTRADA,
                    QUANTIDADE_DISPONIVEL
                FROM LIVROS
                WHERE UPPER(NOME) = %s
            """, (opcao,))

            remocao = cursor.fetchone()

            if remocao:

                cursor.execute("""
                    DELETE FROM LIVROS
                    WHERE CODIGO_ID = %s
                """, (remocao[1],))

                self.conexao_bd.commit()

                print('\nLivro removido com sucesso!')

            else:
                print('\nLivro não encontrado no catálogo.')

        except Exception as erro:
            self.conexao_bd.rollback()
            print(f'\nErro ao remover livro: {erro}')

        finally:
            cursor.close()
