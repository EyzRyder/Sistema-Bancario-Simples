# Sistema Bancário Simples
Este repositório contém um sistema bancário simples implementado em Python. O sistema permite ao usuário realizar operações básicas de banco, como depósito, saque, visualizar extrato e sair do sistema. O objetivo deste projeto é demonstrar conceitos básicos de programação em Python, incluindo controle de fluxo, operações aritméticas, e manipulação de strings.

## Funcionalidades
O sistema oferece as seguintes operações:

1. Depositar: Permite ao usuário depositar um valor na conta bancária. O valor deve ser positivo.
2. Sacar: Permite ao usuário sacar um valor da conta bancária, sujeito a três restrições:
    - O valor do saque não pode exceder o saldo disponível.
    - O valor do saque não pode exceder o limite de R$ 500,00 por operação.
    - O número máximo de saques diários é limitado a 3.
3. Extrato: Exibe o extrato das operações realizadas e o saldo atual da conta.
4. Nova Conta: Permite a criação de uma nova conta bancária associada a um usuário existente.
5. Listar Contas: Exibe todas as contas bancárias cadastradas no sistema.
6. Novo Usuário: Permite a criação de um novo usuário.
7. Sair: Encerra o programa.

## Como Usar
Clone o repositório para o seu ambiente local:
```sh
git clone https://github.com/eyzryder/Sistema-Bancario-Simples.git
```
Navegue até o diretório do projeto:
```sh
cd sistema-bancario-simples
```

Execute o script Python:
```sh
python main.py
```
O menu principal será exibido, permitindo que você escolha entre as opções disponíveis:

```plaintext
=============== MENU ===============
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nc]   Nova Conta
[lc]   Listar Contas
[nu]   Novo Usuario
[q]    Sair

=>
```

5. Siga as instruções na tela para realizar operações de depósito, saque, visualizar extrato ou sair do sistema.

## Exemplo de Uso
- Depositar:
  - Selecione a opção 'd'.
  - Insira o valor do depósito.
- Sacar:
  - Selecione a opção 's'.
  - Insira o valor do saque, certificando-se de que ele não excede o saldo disponível, o limite de saque ou o número de saques permitidos.
- Extrato:
  - Selecione a opção 'e' para visualizar o extrato das transações e o saldo atual.
- Novo Usuário:
  - Selecione a opção 'nu' para criar um novo usuário.
- Nova Conta:
  - Selecione a opção 'nc' para criar uma nova conta associada a um usuário existente.
- Listar Contas:
  - Selecione a opção 'lc' para listar todas as contas cadastradas.
- Sair:
  - Selecione a opção 'q' para encerrar o programa.

## Requisitos
Python 3.x

Feito com ❤️ por Gariel Bessi com DIO
