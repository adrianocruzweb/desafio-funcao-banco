from datetime import datetime
from abc import ABC, abstractmethod

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes[:]

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor
        })

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)

class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # Um cliente tem uma LISTA de contas, apanhei um pouco para entender esse conceito da lista no python

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)
        else:
            print("Erro: A conta informada não pertence a este cliente.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Erro! O valor informado é inválido.")
            return False

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Agência: {self.agencia}\tConta: {self.numero}")
        print("-----------------------------------------")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print("-----------------------------------------")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=========================================")

class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        saldo_total_disponivel = self.saldo + self.limite

        if self.numero_saques >= self.limite_saques:
            print("Erro! Número máximo de saques excedido.")
            return False

        if valor > saldo_total_disponivel:
            print("Erro! Valor do saque excede o saldo e o limite.")
            return False

        if valor <= 0:
            print("Erro! O valor informado é inválido.")
            return False

        self._saldo -= valor
        self.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado! Saques hoje: {self.numero_saques}")
        return True


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Conta
[u] Criar Usuário
[l] Listar Contas
[q] Sair

=> """
####Very old code below, ignore it####
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_cliente = []
lista_contas = []
numero_conta = 1
'''

'''
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
'''

'''
def deposito(saldo, valor, extrato, /):

    saldo_anterior = saldo
    saldo += valor
    extrato += f"\n Depósito: R$ {valor:.2f} | Saldo: R$ {saldo:.2f} | Saldo Anterior: R$ {saldo_anterior:.2f} | {datetime.now()}"
    return saldo, extrato
'''

'''
def imprime_extrato(saldo, /, *, extrato):

    print(extrato)

    return extrato, saldo'''

'''
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
'''

'''
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
'''


'''
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
'''
####Very old code below, ignore it####

class main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            print("--- BLOCO 'd' (DEPOSITAR) INICIADO ---")
            cpf = input("Informe o CPF: ")
            clientes_encontrados = [cliente for cliente in clientes if cliente.cpf == cpf]
            cliente = clientes_encontrados[0] if clientes_encontrados else None
            if cliente and clientes_encontrados[0].contas:
                valor = float(input("Informe o valor do depósito: "))
                deposito = Deposito(valor)
                cliente.realizar_transacao(cliente.contas[0], deposito)
            else:
                print("\nErro! Cliente não encontrado!")

        elif opcao == "s":
            print("--- BLOCO 's' (SACAR) INICIADO ---")
            cpf = input("Informe o CPF: ")
            clientes_encontrados = [cliente for cliente in clientes if cliente.cpf == cpf]
            cliente = clientes_encontrados[0] if clientes_encontrados else None
            if cliente and clientes_encontrados[0].contas:
                valor = float(input("Informe o valor do saque: "))
                saque = Saque(valor)
                cliente.realizar_transacao(cliente.contas[0], saque)
            else:
                print("\nErro! Cliente não encontrado ou não possui conta.")

        elif opcao == "e":
            print("--- BLOCO 'e' (EXTRATO) INICIADO ---")
            cpf = input("Informe o CPF: ")
            clientes_encontrados = [cliente for cliente in clientes if cliente.cpf == cpf]
            cliente = clientes_encontrados[0] if clientes_encontrados else None
            if cliente and clientes_encontrados[0].contas:
                cliente.contas[0].exibir_extrato()
            else:
                print("\nErro! Cliente não encontrado ou não possui conta.")

        elif opcao == "u":
            print("--- BLOCO 'u' (CRIAR CLIENTE) INICIADO ---")
            cpf = input("Informe o CPF (somente números): ")
            cliente_existente = [c for c in clientes if c.cpf == cpf]
            if cliente_existente:
                print("\nErro! Já existe um cliente com este CPF!")
            else:
                nome = input("Informe o nome completo: ")
                data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
                endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

                novo_cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

                print(novo_cliente)
                clientes.append(novo_cliente)
                print("\n Cliente criado com sucesso! ")

        elif opcao == "c":
            print("--- BLOCO 'c' (CRIAR CONTA) INICIADO ---")
            cpf = input("Informe o CPF: ")
            clientes_encontrados = [cliente for cliente in clientes if cliente.cpf == cpf]
            print(clientes_encontrados)
            cliente = clientes_encontrados[0] if clientes_encontrados else None
            if not cliente:
                print("\nErro! Cliente não encontrado! ")
            else:
                numero_conta = len(contas) + 1
                nova_conta = ContaCorrente(numero=numero_conta, cliente=cliente)

                contas.append(nova_conta)
                cliente.adicionar_conta(nova_conta)

                print(f"\n Conta Corrente {numero_conta} Cliente {cliente.nome}! ===")

        elif opcao == "l":
            print("--- BLOCO 'l' (LISTAR CONTA) INICIADO ---")
            if not contas:
                print("\nErro! Nenhuma conta cadastrada. ")
            else:
                print("\n================ LISTA DE CONTAS ================")
                for conta in contas:
                    print(f"""
                    Agência:\t{conta.agencia}
                    Conta:\t\t{conta.numero}
                    Titular:\t{conta.cliente.nome}
                    """)
                print("==============================================")

        elif opcao == "q":
            print("\nSaindo!")
            break

        else:
            print("\n Operação inválida!")
