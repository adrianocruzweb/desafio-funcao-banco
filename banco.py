from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_cliente = []
lista_contas = []
numero_conta = 1


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if(valor < saldo and valor < limite and numero_saques < limite_saques):
        saldo -= valor
        limite -= valor
        numero_saques -= 1
        valor_saque = valor
        valor = 0
        extrato += f"Saque realizado com sucesso: {valor_saque}, Saldo: {saldo} --- {datetime.now()} /n"
    else:
        extrato += f"Tentativa de Saque: {valor_saque}, Saldo: {saldo} --- {datetime.now()} /n"

    return saldo, extrato

def deposito(saldo, valor, extrato, /):

    saldo += valor
    valor_deposito = valor
    valor = 0

    extrato += f"Doposito realizado com sucesso: {valor_deposito}, Saldo: {saldo} --- Saldo Anterior: {saldo-valor} {datetime.now()} /n"

    return saldo, extrato

def imprime_extrato(saldo, /, *, extrato):

    print(extrato)

    return extrato, saldo

def criar_usuario(lista_cliente):

    return lista_cliente

def criar_contas(lista_contas):

    return lista_contas




while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
