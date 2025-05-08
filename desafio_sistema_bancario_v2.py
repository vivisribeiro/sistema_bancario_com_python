import textwrap

def menu():
    menu = """
    ########## MENU ##########
       
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
       
    ##########################
       
    =>   """
    return input (menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        confirma_deposito = f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!"
        print (confirma_deposito)
    else:
        print ("Operação falhou, valor informado inválido.")
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saque_diario):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_saques = numero_saques >= limite_saque_diario

    if excedeu_saldo:
        print ("Operação falhou. Você não tem saldo suficiente!")
            
    elif excedeu_limite:
        print ("Operação falhou. O valor informado excedeu o valor limite de saque.")
            
    elif excedeu_limite_saques:
        print ("Operação falhou. Você excedeu o número de saque diário.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print (f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print(f"\nVocê ainda pode realizar {limite_saque_diario - numero_saques} saque(s) hoje.")

    else:
        print ("Operação falhou. Valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, limite_saque_diario, numero_saques, /, *, extrato):
    print ("########## EXTRATO ##########")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"Saldo: R$ {saldo:.2f}")    
    print (f"Saques restantes hoje: {limite_saque_diario - numero_saques}")
    print ("#############################")

def criar_usuario(usuarios):
    cpf = input ("Informe o CPF (somente números, sem ponto ou traços): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Consta em nosso sistema que esse CPF já possui cadastro")
        return
    
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input ("Endereço (logradouro, n°, bairro - cidade/UF): ")
        
        #adicionar em um dicionario
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print ("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input ("Informe o CPF (somente números, sem ponto ou traços): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}

    print ("Usuário não encontrado, crie o usuario primeiramente.")

def listar_usuarios(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Conta Corrente: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 50)
        print (textwrap.dedent(linha))
     
def main ():
    saldo = 0.0
    limite = 600.0
    extrato = ""
    numero_saques = 0
    limite_saque_diario = 5
    agencia = "0001"
    numero_conta = 1

    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = deposito(saldo, valor, extrato)
                
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque_diario=limite_saque_diario,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, limite_saque_diario, numero_saques, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)
             
        elif opcao == "5":
            conta = criar_conta_corrente(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
       
        elif opcao == "6":
            listar_usuarios(contas)

        elif opcao == "0":
            print ("\n Obrigado por utilizar nosso sistema! Volte sempre.")
            break
        
        else:
            print ("Opção inválida, por favor selecione novamente a operação desejada!")

main()