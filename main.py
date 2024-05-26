from os import system
import textwrap



def menu():
    menu = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo+= valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("!!! Operação falhou! O valor informado é inválido. !!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor> saldo:
        print("!!! Operação falhou! Você não tem saldo suficiente. !!!")

    elif valor>limite:
        print("!!! Operação falhou! O valor do saque excede o limite. !!!")

    elif numero_saques>=limite_saques:
        print("!!! Operação falhou! Número máximo de saques excedido. !!!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$\t{valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("!!! Operação falhou! O valor informado é inválido. !!!")
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf,users):
    usuario_filtrado = [user for user in users if user["cpf"] ==cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_usuario(users):
    cpf = input("Informe o CPF (somente número): ")
    user = filtrar_usuario(cpf,users)

    if user:
        print("\n!!! Já existe usuário com esse CPF! !!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    users.append({
        "nome":nome,
        "data_nascimento":data_nascimento,
        "cpf":cpf,
        "endereco":endereco
        })

    print("=== Usúario criado com sucesso ! ===")

def criar_conta(AGENCIA,numero_conta,users):
    print()

def listar_contas(contas):
    print()

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    users = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo,extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                    )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "nu":
            criar_usuario(users)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA,numero_conta, users)
            if conta: contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        input()
        system("clear")


main()
