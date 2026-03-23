# Sistema de Cadastro de Clientes em Python
Este é um projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python para gerenciamento de clientes via terminal.
O sistema permite cadastrar, listar, atualizar e deletar clientes, além de salvar os dados em arquivos JSON organizados por pastas.

## Funcionalidades
- Cadastrar cliente
- Listar clientes cadastrados
- Atualizar dados de um cliente
- Deletar cliente
- Armazenamento em arquivos .json
- Organização automática em pastas por cliente

## Tecnologias utilizadas
- Python 3
- Biblioteca os (manipulação de diretórios)
- Biblioteca json (armazenamento de dados)

## Estrutura do Projeto
projeto 
┣  clientes_cadastrados 
┃ ┗ Nome_do_Cliente ┃     
┃  ┗ cliente.json 
┗  main.py

## Como funciona
O sistema exibe um menu interativo no terminal:
1 - Cadastrar Cliente
2 - Listar Cliente
3 - Deletar Cliente
4 - Atualizar Cliente
5 - Sair

Cada opção executa uma função específica:
- Cadastrar: adiciona cliente e salva em JSON
- Listar: mostra todos os clientes em memória
- Deletar: remove cliente pelo CPF
- Atualizar: altera dados do cliente

## Aprendizados
- Estruturas de dados (listas e dicionários)
- Manipulação de arquivos JSON
- Organização de código com funções
- Lógica de programação
- CRUD em Python
