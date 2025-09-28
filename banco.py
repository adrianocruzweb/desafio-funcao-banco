from datetime import datetime

class Historico:

    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:

    def registrar(self):
        pass

class Saldo(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self):
        return f"Saldo inicial: R$ {self.valor:.2f} | {datetime.now()}"

class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self):
        return f"Depósito: R$ {self.valor:.2f} | {datetime.now()}"

class cliente:

    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def realizar_transacao(self, conta, transacao):
        conta.saldo += transacao.valor
        conta.historico.adicionar_transacao(transacao.registrar())


    def adicionar_conta(self, Conta):
        self.conta = Conta

class Conta:

    def __init__(self, numero, agencia, Cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = Cliente
        self.saldo = 0
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def nova_conta(self, Cliente, numero):
        self.cliente = Cliente
        self.numero = numero
        self.saldo = 0
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f} | {datetime.now()}")
        return True

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito: R$ {valor:.2f} | {datetime.now()}")
        return True






menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Conta
[u] Criar Usuário
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

    saldo_anterior = saldo

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Erro: Operação falhou! Você não tem saldo suficiente.")
        return False

    elif excedeu_limite:
        print("Erro: Operação falhou! O valor do saque excede o limite.")
        return False

    elif excedeu_saques:
        print("Erro: Operação falhou! Número máximo de saques excedido.")
        return False


    if(valor < saldo and valor < limite and numero_saques < limite_saques):
        saldo -= valor
        limite -= valor
        numero_saques -= 1
        valor_saque = valor
        valor = 0
        extrato += f"\n Saque realizado com sucesso: | Saque: {valor_saque} |( Saldo Atual: {saldo} | Saldo Anterior: {saldo_anterior} )--- {datetime.now()}"
    else:
        extrato += f"\n Tentativa de Saque: {valor_saque} | Saldo Atual: {saldo} --- {datetime.now()}"

    return saldo, extrato

def deposito(saldo, valor, extrato, /):

    saldo_anterior = saldo
    saldo += valor
    extrato += f"\n Depósito: R$ {valor:.2f} | Saldo: R$ {saldo:.2f} | Saldo Anterior: R$ {saldo_anterior:.2f} | {datetime.now()}"
    return saldo, extrato

'''
def imprime_extrato(saldo, /, *, extrato):

    print(extrato)

    return extrato, saldo'''

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
    print(endereco)
    resposta = input("O endereço está correto? (sim/não): ").strip().lower()

    if resposta != "sim":
        return False

    for cliente in lista_cliente:
        if cliente["cpf"] == cpf:
            print("ERRO: CPF já cadastrado.")
            return False

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "conta":[]
    }

    lista_cliente.append(novo_cliente)
    print(lista_cliente)
    print("Usuário cadastrado com sucesso.")

def criar_contas(lista_cliente):
    global numero_conta
    numero_conta += 1

    nova_conta = {
        "agencia": "0001",
        "conta": numero_conta
    }

    for cliente in lista_cliente:
        if cliente["conta"] == nova_conta["conta"]:
            print("ERRO: A conta já está cadastrada para um cliente.")
            return False

    nome = input("informe o nome do cliente:")

    for cliente in lista_cliente:
        if cliente["nome"].lower() == nome.lower():
            print("Cliente encontrado:")
            cliente["conta"].append(nova_conta)
            print("Conta cadastrada com sucesso")
            print(cliente)
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

        saldo,extrato=saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        print(extrato)

    elif opcao == "e":
        imprime_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(lista_cliente)

    elif opcao == "c":
        criar_contas(lista_cliente)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
