# 📚 Sistema de Biblioteca em Python

Sistema de gerenciamento de uma biblioteca desenvolvido em **Python**, com o objetivo de praticar conceitos fundamentais da linguagem, principalmente **funções, listas, dicionários, estruturas de repetição, condicionais e manipulação de dados**.

O projeto permite realizar o cadastro e consulta de clientes e livros, além de controlar empréstimos e devoluções.

---

## 🎯 Objetivo

Este projeto foi desenvolvido como prática de programação em Python e busca simular as principais operações de uma biblioteca através de um sistema executado no terminal.

Durante o desenvolvimento foram praticados conceitos como:

- Funções e parâmetros
- Listas
- Dicionários
- Métodos de listas
- Estruturas `for` e `while`
- Estruturas condicionais `if`, `elif` e `else`
- Entrada e tratamento básico de dados
- Manipulação de estruturas de dados
- Controle de estoque
- Relacionamento entre clientes e livros
- Uso de `return`
- Alteração de dados através de funções

---

## ⚙️ Funcionalidades

O sistema possui um menu principal com as seguintes opções:

### 👤 Cadastro de clientes

Permite cadastrar novos clientes informando:

- Nome
- CPF
- Sobrenome

Também mantém informações sobre:

- Quantidade de livros emprestados
- Livros que estão atualmente com o cliente

Exemplo de estrutura utilizada:

```python
{
    'nome': 'EDUARDO',
    'cpf': 123456,
    'sobrenome': 'SILVA',
    'emprestados': 2,
    'livros': ['HARRY POTTER', 'O HOBBIT']
}
