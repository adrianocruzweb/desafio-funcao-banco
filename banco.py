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
lista_cliente = {}
lista_contas = {}
numero_conta = 1


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if(valor < saldo and valor < limite and numero_saques < limite_saques):
        saldo_anterior = saldo
        saldo -= valor
        limite -= valor
        numero_saques -= 1
        valor_saque = valor
        valor = 0
        extrato += f"Saque realizado com sucesso: | Saque: {valor_saque} |( Saldo Atual: {saldo} | Saldo Anterior: {saldo_anterior} )--- {datetime.now()} /n"
    else:
        extrato += f"Tentativa de Saque: {valor_saque} | Saldo Atual: {saldo} --- {datetime.now()} /n"

    return saldo, extrato

def deposito(saldo, valor, extrato, /):

    saldo_anterior = saldo
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f} | Saldo: R$ {saldo:.2f} | Saldo Anterior: R$ {saldo_anterior:.2f} | {datetime.now()}\n"
    return saldo, extrato


def imprime_extrato(saldo, /, *, extrato):

    print(extrato)

    return extrato, saldo

def criar_usuario(lista_cliente):

    logradouro = input("informe o logradouro: ")
    numero = input("informe o numero: ")
    bairro = input("informe o bairro: ")
    cidade = input("informe o cidade: ")
    estado = input("informe a sigla do estado: ")

    nome = input("Informe o nome do usuário: ")
    aux_cpf = input("Informe o cpf do usuário(sem \".\" e \"-\"): ")
    cpf = aux_cpf.replace(".", "").replace("-", "").strip()

    data_str = input("Informe a data de nascimento (formato dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()
    endereco = f"{logradouro},{numero} - {bairro} - {cidade}/{estado}"

    for cliente in lista_cliente:
        if cliente["cpf"] == cpf:
            print("ERRO: CPF já cadastrado.")
            return False

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    lista_cliente.append(novo_cliente)
    print("Usuário cadastrado com sucesso.")

def criar_contas():
    global numero_conta
    numero_conta += 1

    nova_conta = {
        "agencia": "0001",
        "conta": numero_conta
    }

    for cliente in lista_cliente:
        if cliente["conta"]["conta"] == nova_conta["conta"]:
            print("ERRO: A conta já está cadastrada para um cliente.")
            return False

    nome = input("informe o nome do cliente:")

    for cliente in lista_cliente:
        if cliente["nome"].lower() == nome.lower():
            print("Cliente encontrado:")
            cliente["conta"].append(nova_conta)
            print("Conta cadastrada com sucesso")
            return True

    print("Cliente não encontrado.")
    return False



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo,extrato=deposito(saldo, valor, extrato)

        print(extrato)

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
