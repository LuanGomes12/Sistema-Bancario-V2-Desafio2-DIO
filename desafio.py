# Funções
# Função para criar o Menu
def menu():
    menu ="""
    ===== MENU =====
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar usuário
    [5] - Cadastrar conta
    [0] - Sair
    ================
    =>"""

    return input(menu)

# Função sacar, recebe os parâmetros apenas por palavra chave (keyword only)
def saque(*, saldo, valor, numero_saques, limite_saques, limite_maximo_saque, extrato):

    excedeu_saque = valor > saldo
    excedeu_limite_saque = valor > limite_maximo_saque
    excedeu_numero_saques = numero_saques >= limite_saques

    if excedeu_saque:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite_saque:
        print("Operação falhou! Valor informado excede o limite de saque diário (R$500,00 reais).")

    elif excedeu_numero_saques:
        print("Operação falhou! Número limite de saques diários antigido. Você só poderá sacar novamente em 24 horas!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("Operação realizada com sucesso!")

    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato, numero_saques

# Função depositar, recebe os parâmetros apenas por posição (positional only)
def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}"
        print("Operação realizada com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")  

    return saldo, extrato

# Exibir extrato, retorno vazio (None)
def exibir_extrato(saldo, /, *, extrato):
    print("\n==== EXTRATO ====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"Saldo: R$ {saldo:.2f}")
    print("=================")
    

def cadastrar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Esse CPF já foi cadastrado!")
        return
    
    nome = input("Nome completo:")
    data_nascimento = input("Data de Nascimento (dd-mm-aaaa):")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

# Verificar se já existe um usuário cadastrado com o CPF informado
def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        else:
            return None

def cadastrar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")

def main():
    saldo = 0
    limite_maximo_saque = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Quanto você deseja depositar?"))

            saldo, extrato =  deposito(saldo, valor, extrato)

        elif opcao == "2":

            valor = float(input("Quanto você deseja sacar?"))

            saldo, extrato, numero_saques = saque(
                saldo = saldo, 
                valor = valor,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES_DIARIOS,
                limite_maximo_saque = limite_maximo_saque,
                extrato = extrato,
                )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato= extrato)

        elif opcao == "4":

            cadastrar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "0":
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Operação inválida! Digite novamente a operação desejada!")

main()
