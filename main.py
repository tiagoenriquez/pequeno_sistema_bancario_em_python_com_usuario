from datetime import date

class Usuario:

    def __init__(
            self,
            nome: str,
            nascimento: str,
            cpf: str,
            endereco: str
            ) -> None:        
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:

    def __init__(self, numero: int, usuario: Usuario) -> None:
        self.numero = numero
        self.usuario: Usuario = usuario
        self.AGENCIA = "0001"
        self.saldo = 0.0
        self.movimentacoes: list[float] = []
        self.data_do_ultimo_saque = date.today()
        self.qtd_saques_hoje = 0
        
    def _validar_valor_positivo(self, valor: float) -> None:

        if valor <= 0:
            mensagem = "Não é possível realizar a operação com valor negativo."
            mensagem += " Operação cancelada."
            raise Exception(mensagem)
    
    def depositar(self, valor: float, /) -> None:
        self._validar_valor_positivo(valor)
        self.saldo += valor
        self.movimentacoes.append(valor)
    
    def sacar(self, *, valor: float) -> None:
        SAQUE_MAXIMO = 500
        LIMITE_DE_SAQUES = 3
        self._validar_valor_positivo(valor)
        if valor > SAQUE_MAXIMO:
            raise Exception("Valor maior do que permitido para saque.")
        if valor > self.saldo:
            raise Exception("Saldo insuficiente.")
        ultimo_saque_foi_hoje = self.data_do_ultimo_saque == date.today()
        if self.qtd_saques_hoje == LIMITE_DE_SAQUES and ultimo_saque_foi_hoje:
            raise Exception("Número máximo de saques atingido")
        self.saldo -= valor
        self.movimentacoes.append(0 - valor)
        if ultimo_saque_foi_hoje:
            self.qtd_saques_hoje += 1
        else:
            self.data_do_ultimo_saque = date.today()
            self.qtd_saques_hoje = 0
        
    def visualizar_extrato(self) -> str:
        extrato = "\n\nMovimentações:\n"
        for movimentacao in self.movimentacoes:
            if movimentacao > 0:
                extrato += f"Depósito de R$ {movimentacao:.2f}\n"
            else:
                extrato += f"Saque    de R$ {0 - movimentacao:.2f}\n"
        extrato += f"\nSaldo: R$ {self.saldo:.2f}\n\n"
        return extrato

usuarios: list[Usuario] = []
contas: list[Conta] = []

def imprimir_titulo(titulo: str) -> None:
    titulo = titulo.upper().center(len(titulo) + 2, ' ').center(80, '#')
    print(f"\n{titulo}\n")

def imprimir_erro(erro: str) -> None:
    mensagem = erro.center(len(erro) + 2, ' ')
    mensagem = mensagem.center(len(mensagem) + 6, '@')
    print(f"\n{mensagem}\n")

def imprimir_sucesso(sucesso: str) -> None:
    mensagem = sucesso.center(len(sucesso) + 2, ' ')
    mensagem = mensagem.center(len(mensagem) + 6, '|')
    print(f"\n{mensagem}\n")

def adicionar_usuario() -> None:
    imprimir_titulo("Cadastro de Usuário")
    nome = input("Nome: ")
    nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ").replace(".", "").replace("-", "")
    endereco = input("Endereço: ")

    if cpf in [usuario.cpf for usuario in usuarios]:
        erro = "Já existe usuário com o CPF informado. Operação cancelada"
        imprimir_erro(erro)
        return None
    
    usuario = Usuario(nome, nascimento, cpf, endereco)
    usuarios.append(usuario)
    sucesso = "Usuário cadastrado com sucesso"
    imprimir_sucesso(sucesso)

def listar_usuarios() -> None:
    imprimir_titulo("Lista de Usuários")

    for usuario in usuarios:
        print(f"Usuário: {usuario.nome}")
        print(f"Data de Nascimento: {usuario.nascimento}")
        print(f"Endereço: {usuario.endereco}")
        print("\n")
        print("Contas:")

        for conta in contas:
            if conta.usuario == usuario:
                print(f"Nº: {conta.numero}")

        print("\n")

def obter_usuario(cpf: str) -> Usuario | None:

    for usuario in usuarios:

        if usuario.cpf == cpf:
            return usuario
        
    return None

def adicionar_conta() -> None:
    imprimir_titulo("Criação de Conta Bancária")
    cpf = input("Informe seu CPF: ").replace(".", "").replace("-", "")
    usuario = obter_usuario(cpf)

    if usuario == None:
        erro = "Usuário não cadastrado"
        imprimir_erro(erro)
        return None
    
    conta = Conta(len(contas) + 1, usuario)
    contas.append(conta)
    sucesso = "Conta adicionada com sucesso"
    imprimir_sucesso(sucesso)

def obter_conta(numero: int) -> Conta | None:

    for conta in contas:

        if conta.numero == numero:
            return conta
        
    return None

def validar_conta_de_usuario() -> Conta | None:
    n_conta = int(input("Digite o nº da conta: "))
    conta = obter_conta(n_conta)

    if conta == None:
        erro = "Conta não existe"
        imprimir_erro(erro)
        return None
    
    cpf = input("Digite o CPF: ").replace(".", "").replace("-", "")
    usuario = obter_usuario(cpf)

    if conta.usuario != usuario:
        erro = "A conta não pertence ao usuário"
        imprimir_erro(erro)
        return None
    
    return conta    

def depositar() -> None:
    imprimir_titulo("Depósito")
    conta = validar_conta_de_usuario()

    if conta != None:
        valor = float(input("Digite o valor: "))

        try:
            conta.depositar(valor)
            sucesso = "Valor depositado com sucesso"
            imprimir_sucesso(sucesso)
        except Exception as erro:
            imprimir_erro(str(erro))

def sacar() -> None:
    imprimir_titulo("Saque")
    conta = validar_conta_de_usuario()

    if conta != None:
        valor = float(input("Digite um valor: "))
        
        try:
            conta.sacar(valor=valor)
            sucesso = "Valor liberado. Pode retirar as cédulas."
            imprimir_sucesso(sucesso)
        except Exception as erro:
            imprimir_erro(str(erro))

def visualizar_extrato() -> None:
    imprimir_titulo("Extrato")
    conta = validar_conta_de_usuario()

    if conta != None:
        print(conta.visualizar_extrato())

def menu() -> None:
    opcao = "a"
    mensagem = """
Digite sua opção:
[d] - Depositar
[s] - Sacar
[e] - Extrato
[u] - Novo usuário
[l] - Lista de usuarios
[c] - Nova conta
[q] - Sair

"""

    while opcao != "q":
        imprimir_titulo("Sistema Bancário")
        opcao = input(mensagem)
        
        if opcao == "u":
            adicionar_usuario()
        if opcao == "l":
            listar_usuarios()
        if opcao == "c":
            adicionar_conta()
        if opcao == "d":
            depositar()
        if opcao == "s":
            sacar()
        if opcao == "e":
            visualizar_extrato()

menu()