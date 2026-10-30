# 📚 Sistema de Biblioteca em Python

Sistema de gerenciamento de biblioteca desenvolvido em **Python** para praticar conceitos fundamentais da linguagem, como funções, listas, dicionários, estruturas condicionais e de repetição.

## ⚙️ Funcionalidades

- 👤 Cadastro de clientes
- 🔎 Consulta de clientes por nome ou CPF
- 📖 Cadastro de livros
- 🔍 Consulta de livros por nome, autor ou ano
- 📤 Empréstimo de livros
- 📥 Devolução de livros
- 📊 Controle de quantidade disponível
- 📝 Registro dos livros em posse de cada cliente
- 🗑️ Remoção de livros
- ➕ Alteração da quantidade de livros cadastrados

## 🧠 Conceitos praticados

- Funções e parâmetros
- Listas e dicionários
- Métodos `append()` e `remove()`
- Estruturas `for` e `while`
- Condicionais `if`, `elif` e `else`
- Variáveis booleanas
- Manipulação de dados entre funções

## 💻 Tecnologias

- Python 3
- Terminal/Console
- Sem bibliotecas externas

## ⚠️ Observação

Atualmente, os dados são armazenados apenas durante a execução do programa. Ao encerrá-lo, os dados cadastrados são perdidos.

## 🚀 Próximos passos

- Persistência de dados com SQL - FEITO
- Implementação de banco de dados - FEITO
- Validação de CPF - FEITO
- Melhor tratamento de erros - FEITO
- Interface gráfica
- Programação Orientada a Objetos - FEITO

## 🆕 Atualizações do projeto

### 🔄 Versão 2.0 — Evolução do sistema

O projeto passou por uma reestruturação para melhorar a organização do código e o gerenciamento das informações.

**Principais mudanças:**

- 🗄️ **Banco de dados PostgreSQL:** substituição do armazenamento temporário em listas e dicionários por persistência em banco de dados.
- 🧱 **Programação Orientada a Objetos (POO):** reorganização das funcionalidades em uma classe responsável pelo gerenciamento da biblioteca.
- 👤 **Cadastro de clientes aprimorado:** inclusão de data de nascimento, telefone, e-mail e validação de CPF.
- 📚 **Cadastro de livros aprimorado:** inclusão de código identificador, data de lançamento e controle de quantidades cadastradas e disponíveis.
- 🔎 **Consultas com SQL:** pesquisas de livros e clientes realizadas diretamente no banco de dados.
- 🔄 **Empréstimos e devoluções:** operações integradas ao banco de dados, com atualização das quantidades disponíveis.
- 🛡️ **Tratamento de erros:** implementação de exceções e operações de confirmação ou reversão de transações com `commit()` e `rollback()`.
- 🧩 **Organização do código:** separação de funcionalidades auxiliares e da conexão com o banco de dados em módulos próprios.

**Objetivo da atualização:** evoluir de um projeto introdutório de Python para uma aplicação mais estruturada, aplicando conceitos de POO, SQL e integração com banco de dados relacional.
 
## 👨‍💻 Autor

- Eduardo Silva

 Projeto desenvolvido para prática e evolução dos conhecimentos em Python.
