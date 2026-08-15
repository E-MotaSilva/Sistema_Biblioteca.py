#funcao para cadastro de cliente
def cadastrocliente(consulta2): #chamei a variavel aqui para que ela possa registrar as alteracoes que podem ser feitas por meio da funcao emprestarlivro e devolverlivro
    print('==Cadastro de clientes==')
    opcao = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower() #entrada de dados, strip para retirar espacos no inicio e no fim e lower para definir todas as letras em minuscula

    while opcao != 'sim' and opcao != 'nao': #estrutura de repeticao para que repita caso a resposta seja diferente de sim e nao
        print('Tente novamente! Opcoes possiveis: Sim ou Nao')
        opcao = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower()

    if opcao == 'sim': #condicional para resposta sim

        while True: #repeticao booleana para que o o cadastro so termine caso seja digitada a opcao nao
            nome = str(input('Digite seu nome: ')).strip().upper()
            cpf = int(input('Digite seu cpf: '))
            sobrenome = str(input("Digite os sobrenomes: ")).strip().upper()

            pessoas = {'nome': nome, 'cpf': cpf, 'sobrenome': sobrenome, 'emprestados': 0, 'livros': []} #dicionario com os dados  do cliente, lista em livors para receber as informacoes quando o livro for emprestado para o cliente

            consulta2.append(pessoas) #aqui uma lista consulta2 que recebe o dicionario pessoas, possibilitando consultas e alteracoes aqui e em outros pontos do codigo

            print('Cadastro realizado com sucesso!')

            opcao = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower()

            while opcao != 'sim' and opcao != 'nao':
                print('Tente novamente! Opções possíveis: Sim ou Não')
                opcao = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower()

            if opcao == 'nao':
                print('Retornando para o menu anterior...!')
                break #para que a repeticao seja interrompida

def consultacliente(consulta2): #chamei consulta2 aqui para poder usar nas estruturas de repeticao abaixo na consulta
    print('\n==Consulta de clientes==\n')
    print('1 - Procurar por cpf')
    print('2 - Procurar por nome')
    print('3 - Voltar para o menu anterior')
    escolha = int(input('Escolha uma opcao: '))

    while escolha != 3: #repete enquanto a escolha for diferente de 3

        if escolha == 1: 
            procurar = int(input('Digite o cpf: '))

            for pessoa in consulta2: #for para percorrer a lista consulta2 e mostrar infos
                if pessoa['cpf'] == procurar:
                    print()
                    print('-'*10)
                    print(f'NOME: {pessoa["nome"]}') #mostra o nome associado ao cpf digitado
                    print(f'SOBRENOME: {pessoa["sobrenome"]}') #mostra o sobrenome associado ao cpf digitado
                    if pessoa["emprestados"] > 0: #condicional para verificar se o cliente esta com algum livro caso sim executa
                        print(f'EM POSSE DE {pessoa["emprestados"]} LIVROS') #mostra a quantidade de livros
                        print(f'LIVROS: {pessoa["livros"]}') #mostra o nome do livro
                    print('-' * 10)
                    print()
                    break #interromper o fluxo
            else:
                print('Nenhum cpf foi encontrado!')
        elif escolha == 2:
            procurar = str(input('Digite o nome: ')).strip().upper()

            for pessoa in consulta2:
                if pessoa['nome'] == procurar:
                    print()
                    print('-' * 10)
                    print(f'CPF: {pessoa["cpf"]}')
                    print(f'SOBRENOME: {pessoa["sobrenome"]}')
                    if pessoa["emprestados"] > 0:
                        print(f'EM POSSE DE {pessoa["emprestados"]} LIVROS')
                        print(f'LIVROS {pessoa["livros"]}')
                    print('-' * 10)
                    print()
                    break
            else:
                print('Nenhum nome foi encontrado!')

        elif escolha == 3:
            print('Voltando para o menu anterior...')
        else:
            print('Opcao invalida!')

        print('==Consulta de clientes==\n')
        print('1 - Procurar por cpf')
        print('2 - Procurar por nome')
        print('3 - Voltar para o menu anterior')
        escolha = int(input('Escolha uma opcao: '))

def cadastrarlivro(consulta): #consulta chamado aqui para que possa ser acessada em outros lugares do codigo, e para que o cadastro realizado em emprestarlivro seja de fato guardado nessa lista e nao em uma nova lista existente apenas na funcao emprestarlivro

    print('\n==Cadastrar livro==\n')
    choice = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower()

    while choice != 'sim' and choice != 'nao':
        print('Tente novamente! Opcoes possiveis: Sim ou Nao')
        choice = str(input('Deseja realizar um novo cadastro? [SIM/NAO]: ')).strip().lower()

    if choice == 'sim':

        while True:

            print('\n==Cadastrar livro==\n')
            nome = str(input('Nome do livro: ')).strip().upper()
            autor = str(input('Autor do livro: ')).strip().upper()
            ano = int(input('Ano do livro: '))
            disponivel = int(input('Quantos disponiveis?: '))

            livros = {'nome': nome, 'autor': autor, 'ano': ano, 'disponibilidade': disponivel, 'quantidadecadastrada': disponivel}
            consulta.append(livros)

            choice = str(input('Livro cadastrado com sucesso! Deseja continuar? [SIM/NAO]: ')).strip().lower()

            while choice != 'sim' and choice != 'nao':
                print('Tente novamente! Opções possíveis: Sim ou Não')
                choice = input('Deseja realizar um novo cadastro? [SIM/NAO]: ').strip().lower()

            if choice == 'nao':
                print('Voltando para o menu anterior...')
                break

def verificandolivro(consulta):
    print('\n==Verificar livro==\n')
    print('1 - Procurar por nome')
    print('2 - Procurar por ano')
    print('3 - Procurar por autor')
    print('4 - Voltar para o menu anterior')

    escolha = int(input('Escolha uma opcao: '))

    while escolha != 4: #repeticao so encerra ao escolher a opcao 4

        if escolha == 1:
            nome = str(input('Digite o nome do livro: ')).strip().upper()

            encontrou = False #variavel comeca falso mas transforma em verdadeiro caso o for abaixo encontrar o nome digitado

            for livro in consulta:
                if livro["nome"] == nome:
                    encontrou = True

                    #acessa as informaceos na lista
                    print()
                    print('-' * 10)
                    print(f'AUTOR: {livro["autor"]}')
                    print(f'ANO: {livro["ano"]}')
                    print(f'EXISTEM {livro["disponibilidade"]} LIVROS DISPONIVEIS')
                    print(f'{livro["quantidadecadastrada"] - livro["disponibilidade"]} LIVROS FORAM EMPRESTADOS')
                    print('-' * 10)
                    print()

            if not encontrou: #caso nao se torne True printa a info abaixo
                    print('\nLivro nao encontrado!\n')

        elif escolha == 2:
        #mesma aplicacao mas procurando por ano do livro
            anolivro = int(input('Digite o ano do livro: '))

            encontrou = False

            for ano in consulta:
                if ano["ano"] == anolivro:
                    encontrou = True

                    print()
                    print('-' * 10)
                    print(f'AUTOR: {ano["autor"]}')
                    print(f'LIVRO: {ano["nome"]}')
                    print(f'EXISTEM {ano["disponibilidade"]} LIVROS DISPONIVEIS')
                    print(f'{ano["quantidadecadastrada"] - ano["disponibilidade"]} LIVROS FORAM EMPRESTADOS')
                    print('-' * 10)
                    print()

            if not encontrou:
                print('\nAno nao registrado!\n')

        elif escolha == 3:
        #procurando por autor
            autor = str(input('Digite o autor do livro: ')).strip().upper()

            encontrou = False

            for autorlivro in consulta:

                if autorlivro['autor'] == autor:
                    encontrou = True

                    print()
                    print('-' * 10)
                    print(f'LIVRO: {autorlivro["nome"]}')
                    print(f'ANO: {autorlivro["ano"]}')
                    print(f'EXISTEM {autorlivro["disponibilidade"]} LIVROS DISPONIVEIS')
                    print(f'{autorlivro["quantidadecadastrada"] - autorlivro["disponibilidade"]} LIVROS FORAM EMPRESTADOS')
                    print('-' * 10)
                    print()

            if not encontrou:
                print('\nAutor nao encontrado!\n')

        elif escolha == 4:
            print('Voltando para o menu anterior...')

        else:
            print('Opcao invalida!')

        print('\n==Verificar livro==\n')
        print('1 - Procurar por nome')
        print('2 - Procurar por ano')
        print('3 - Procurar por autor')
        print('4 - Voltar para o menu anterior')

        escolha = int(input('Escolha uma opcao: '))

def emprestarlivro(consulta, consulta2): #aqui a funcao acessa consulta e consulta 2 para que os dados possam ser lidos e adicionados a essas listas

    print('\n==Emprestar livro==\n')

    destino = str(input('Digite o nome do cliente: ')).strip().upper()

    cliente_encontrado = False

    for cliente in consulta2:

        if cliente["nome"] == destino:
            cliente_encontrado = True

            print(f'O livro esta sendo emprestado para {cliente["nome"]}!')
            print('-' * 10)
            break
    #aqui nessa condicional o usuario tem a opcao de cadastrar o cliente caso ele nao seja encontrado na busca. principalmente por causa dessa funcao e da outra abaixo que chamei as listas na nomenclatura da funcao
    if not cliente_encontrado:
        print('Cliente não encontrado!')
        cadastrar = str(input('Cadastrar o cliente agora? [SIM/NAO]: ')).strip().upper()
        if cadastrar == 'SIM':
            cadastrocliente(consulta2)
        elif cadastrar == 'NAO':
            print('Retornando...')
        else:
            print('Opcao invalida!')
        return

    emprestar = str(input('Qual livro deseja emprestar?: ')).strip().upper()

    livro_encontrado = False

    for livro in consulta:

        if livro["nome"] == emprestar:
            livro_encontrado = True

            print('-' * 10)
            print(f'AUTOR: {livro["autor"]}')
            print(f'ANO: {livro["ano"]}')
            print(f'QUANTIDADE DISPONIVEL: {livro["disponibilidade"]}')
            print('-' * 10)

            saida = int(input('Quantidade a ser emprestada?: '))

            if livro["disponibilidade"] >= saida:
                livro["disponibilidade"] -= saida
                print('Quantidade emprestada com sucesso!')
                cliente["emprestados"] += saida
                cliente["livros"].append(livro["nome"])
                break

            else:
                print('Quantidade solicitada indisponível!')
            break
    if not livro_encontrado:
        print('Livro não encontrado!')
        cadastrar = str(input('Deseja cadastrar agora? [SIM/NAO]: ')).strip().upper()
        if cadastrar == 'SIM':
            cadastrarlivro(consulta)
        elif cadastrar == 'NAO':
            print('Retornando...')
        else:
            print('Opcao invalida!')
        return

def devolverlivro(consulta, consulta2):
    print('\n==Devolucao do livro==\n')

    nome_cliente = False
    locador = str(input('Digite o nome do cliente que ira devolver: ')).strip().upper()

    for devolver in consulta2:
        if devolver["nome"] == locador:
            nome_cliente = True

            emprestar = str(input('Qual livro deseja recolocar?: ')).strip().upper()
            for livro in consulta:
                if livro["nome"] == emprestar:
                    print('-' * 10)
                    print(f'AUTOR: {livro["autor"]}')
                    print(f'ANO: {livro["ano"]}')
                    print(f'QUANTIDADE DISPONIVEL: {livro["disponibilidade"]}')
                    print('-' * 10)
                    entrada = int(input('Quantidade a ser devolvida?: '))
                    if entrada > 0:
                        if entrada + livro["disponibilidade"] <= livro["quantidadecadastrada"]:
                            livro["disponibilidade"] += entrada
                            devolver["livros"].remove(emprestar)
                            devolver["emprestados"] -= entrada
                            print('Quantidade devolvida com sucesso!')
                            print(f'Ainda existem {livro["quantidadecadastrada"] - livro["disponibilidade"]} para serem devolvidos!')
                        else:
                            print('Devolucao nao efetuada. Quantidade maior do que cadastro.')

                else:
                    print('Opcao invalida')
                break
            else:
                print('Livro não encontrado!')
    if not nome_cliente:
        print('Cliente nao localizado')

def removerlivro(consulta):

    print('\n==Remover livro==\n')
    print('O que deseja fazer?:')
    print('1 - Alterar quantidade de livros')
    print('2 - Remover livro da biblioteca')
    print('3 - Voltar para o menu anterior')
    escolha = int(input('Escolha uma opcao: '))

    while escolha != 3:

        if escolha == 1:

            remover = str(input('Qual livro alterar quantidade disponivel?: ')).strip().upper()

            livro_encontrado = False

            for livro in consulta:

                if livro["nome"] == remover:
                    livro_encontrado = True

                    quantidade = int(input('Quantidade a ser removida?:: '))

                    if quantidade <= livro["quantidadecadastrada"]:

                        livro["quantidadecadastrada"] -= quantidade
                        livro["disponibilidade"] -= quantidade
                        print('Quantidade removida com sucesso!')
                        print(f'Novo estoque: {livro["quantidadecadastrada"]}')
                    else:
                        print('Quantidade indisponivel para remocao!')

            if not livro_encontrado:
                print('Livro nao encontrado!')
                return

        elif escolha == 2:

            remover = str(input('Qual livro deseja excluir?: ')).strip().upper()

            livro_encontrado = False

            for livro in consulta:
                if livro["nome"] == remover:

                    livro_encontrado = True

                    excluir = str(input('Confirma exclusao? [SIM/NAO] (Essa acao nao podera ser desfeita): ')).strip().upper()

                    if excluir == 'SIM':
                        print('\nExclusao concluida com sucesso!')
                        consulta.remove(livro)
                        break

                    elif excluir == 'NAO':
                        print('Exclusao cancelada!')

                    else:
                        print('Opcao invalida!')

                if not livro_encontrado:
                    print('Livro nao encontrado!')
                    return

        print('\n==Remover livro==\n')
        print('O que deseja fazer?:')
        print('1 - Alterar quantidade de livros')
        print('2 - Remover livro da biblioteca')
        print('3 - Voltar para o menu anterior')
        escolha = int(input('Escolha uma opcao: '))

def iniciar():
    print('==Bem vindo a biblioteca==')
    print('1 - Cadastrar cliente') #ok
    print('2 - Consultar cliente') #ok
    print('3 - Verificar livros disponiveis') #meio ok
    print('4 - Emprestar livro') #meio ok
    print('5 - Devolver livro') #meio ok
    print('6 - Adicionar livro') #ok
    print('7 - Remover livro')
    print('8 - Sair do sistema')

    escolha = int(input('Escolha o que deseja fazer: '))
    consulta2 = []
    consulta = []

    while escolha != 8:
        if escolha == 1:
            cadastrocliente(consulta2)
        elif escolha == 2:
            consultacliente(consulta2)
        elif escolha == 3:
            verificandolivro(consulta)
        elif escolha == 4:
            emprestarlivro(consulta, consulta2)
        elif escolha == 5:
            devolverlivro(consulta, consulta2)
        elif escolha == 6:
            cadastrarlivro(consulta)
        elif escolha == 7:
            removerlivro(consulta)
        else:
            print('Opcao invalida')

        print('==Bem vindo a biblioteca==')
        print('1 - Cadastrar cliente')
        print('2 - Consultar cliente')
        print('3 - Verificar livros disponiveis')
        print('4 - Emprestar livro')
        print('5 - Devolver livro')
        print('6 - Adicionar livro')
        print('7 - Remover livro')
        print('8 - Sair do sistema')
        escolha = int(input('Escolha o que deseja fazer: '))
    print('Encerrando o sistema...')

iniciar()
