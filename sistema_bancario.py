#Fomos contratados por um grande banco para desenvolver o seu novo sistema.
#Esse Banco deseja modernizar suas operações e para isso escolheu a linguagem python.
#Para a primeira versão do sistema devemos implementar apenas 3 operações: Depósito, saque e extrato.
#Depósito:
#Deve ser possível depositar valores positivos na conta. #A V1 trabalha com apenas 1 usuário. Todos os depósitos devem ser armazenados em uma variável
#Saques:
#3 saques diários com limite de R$500,00 por saque. Se o usuário não tiver saldo em conta, deve exibir uma mensagem inforando que não
#será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser amazenados em uma variável e exibidos na opção de extrato.
#Extrato:
#Listar todos os depósitos e saques realiados na conta. No final da listagem, exibir o saldo atual da conta.
#Os valores devem ser exibidos no formato R$ xxx.xx, exemplo 1500.45 = R$ 1500.45,00

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
num_saques = 0

inicial = """
Digite aqui a operação que deseja realizar!
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
"""
while True:
    print(inicial)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso\n"
        else:
            print("Valor inválido. O depósito deve ser maior que 0")    
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
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
    elif opcao == 3:
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
    elif opcao == 4:
            print("Saindo do sistema...\n")
            break
    else:
        print("Opção inválida. Digite novamente!\n")
            