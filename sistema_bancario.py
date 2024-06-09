#Criar funções para todas as operações do sistema
#Saque: receber argumentos por nome (keyword only)
#Depósito: receber argumento por posição (position only)
#Extrat0: receber argumento por posição e keyword
#Novas funções para criar: Criar usuário e criar conta
#Criar usuário: armazenar usuários em lista, composta por nome, data de nascimento, cpf e endereço. Endereço é string no formato
# logradouro, nro - bairro - cidade/sigla do Estado. Armazenar apenas numero do CPF. Não pode cadastrar usuário com mesmo CPF
# (CPF deve ser chave do dicionário de endereço)
#Criar conta conta: armazanar contas correntes em lista composta por agencia, numero da conta e usuario. Numero da conta é sequencial, 
# iniciando em 1. O numero da agencia é fixo "0001". O usuário pode ter mais de uma conta, mas uma conta pode pertencer a apenas 1 usuário
import re

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
num_saques = 0
usuarios = []
contas = ["01234", "23456"]
conta_atual = None
num_conta = None
extrato = None

def login():
    print("Acesse sua conta digitando sua agencia e conta corrente.\n")

    agencia_input = str(input("Digite sua agência: "))
    while agencia_input != "0001" and agencia_input != "0000":
        agencia_input = str(input("A agência não existe. Informe uma agência válida. Para sair, digite Sair.\n"))
        if agencia_input == "0001":
            True
        elif agencia_input.lower() == "sair":
            return None
    agencia = agencia_input
    conta_input = str(input("Informe sua conta corrente: "))
    while conta_input not in contas:
        conta_input = str(input("A conta não existe em nosso banco de dados. Informe uma conta válida. Para sair, digite Sair.\n"))
        
        if conta_input.lower() == "sair":
           return None
    
    conta = contas[contas.index(conta_input)]
    
    return agencia, conta

def oper_iniciais_user(conta):
    operacoes_msg = """
    Digite aqui a operação que deseja realizar!
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Criar Conta
    4 - Sair
    \n
    """
    print(operacoes_msg)
    opcao = int(input())
    operacoes(opcao, conta)
    return opcao

def oper_iniciais_ger(conta):
    operacoes_msg = """
    Digite aqui a operação que deseja realizar!
    1 - Extrato
    2 - Criar Conta
    3 - Criar Usuário
    4 - Sair
    \n
    """
    print(operacoes_msg)
    opcao = int(input())
    operacoes(opcao, conta)
    return opcao

def operacoes(opcao, conta):
    if opcao == 1:
        return deposito(conta)
    elif opcao == 2:
        saque(conta)
    elif opcao == 3:
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
    elif opcao == 4:
            print("Saindo do sistema...\n")
            return None
    else:
        print("Opção inválida. Digite novamente!\n")
            
def criar_conta(cpf):
    if usuarios[cpf]:
        global num_conta 
        num_conta = contas[-1][1]
        num_conta = str(int(num_conta + 1))
        nova_conta = {
            "agencia": "0001",
            "numero_conta": num_conta,
            "cpf": cpf
        }
        contas.append(nova_conta)
        return True, "Conta criada com sucesso."
    else:
        print(f"o CPF{cpf} não está cadastrado no nosso banco.\n", "Deseja cadastrar este cpf no banco?")
        return "Não foi possível criar a conta."

def criar_usuario(cpf):
    if usuarios[cpf]:
        print("CPF já existe em nossa base de dados.")
    else:
        nome = input("Informe o nome do novo Usuário: ")
        while not re.match(r"^[a-zA-Z\s]+$", nome):
            print("O nome deve conter apenas letras e espaços.")
            nome = input("Informe o nome do novo Usuário: ")
            
        dt_nasc = input("Informe a data de nascimento do usuário no formato dd/mm/aaaa: ")
        while not re.match(r"^\d{2}/\d{2}/\d{4}$", dt_nasc):
            print("Formato de data inválido. Use o formato dd/mm/aaaa.")
            dt_nasc = input("Informe a data de nascimento do usuário no formato dd/mm/aaaa: ")
            
        endereco = input("Informe o endereço do usuário. Logradouro, número, bairro e cidade/sigla do Estado")
        match = re.match(r"^(.+), (\d+), (.+), ([a-zA-Z\s]+)/([A-Z]{2})$", endereco)
        while not match:
            print("Formato de endereço inválido.")
            endereco = input("Informe o endereço do usuário. Logradouro, número, bairro e cidade/sigla do Estado")
            
        if match:
            logradouro, numero, bairro, cidade, estado = match.groups()
            endereco_formatado = f"{logradouro}, {numero}, {bairro}, {cidade}/{estado}"

        usuarios[cpf] = {
            "nome": nome,
            "dt_nascimento": dt_nasc,
            "endereco": endereco            
        }
    
    return True, "Usuário cadastrado."
        

def deposito(cc):
    valor = float(input("Digite o valor do depósito: "))
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso\n"
    else:
        print("Valor inválido. O depósito deve ser maior que 0")          

def saque(cc=contas):
    valor = float(input("Digite o valor do saque: "))
    global saldo, extrato, num_saques
    if valor > 0 and valor <= limite and valor <= saldo and num_saques <= LIMITE_SAQUES:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f} realizado com sucesso\n"
        num_saques += 1
        print(f"Valor sacado. Saldo restante de {saldo}\n")
    elif valor <= 0:
        print(f"Valor inválido. O valor do saque deve ser maior que 0 e menor que R$ {limite:.2f}\n")
    elif valor > limite:
        print(f"Valor limite de saque excedido!")
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
    elif num_saques > LIMITE_SAQUES:
        print(f"Limite de saques diários excedido! Você só pode realizar {LIMITE_SAQUES} saques por dia\n")        

def extrato(cpf, conta=contas):
    global extrato, saldo
    print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}\n")    
    
agencia_logada, conta_autenticada = login()

if conta_autenticada:
    if agencia_logada == "0001":
        oper = oper_iniciais_user(conta_autenticada)
    elif agencia_logada == "0000":
        oper = oper_iniciais_ger(conta_autenticada)