menu = """
    ########## MENU ##########
       
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [0] Sair
       
    ##########################
       
    =>   """

saldo = 0.0
limite = 600.0
extrato = ""
numero_saques = 0
limite_saque_diario = 5

nome = input("Informe seu nome para iniciar: ")
print(f"\nBem-vindo ao seu banco, {nome}! O que deseja realizar hoje?")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            confirma_deposito = f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!"
            print (confirma_deposito)

        else:
            print ("Operação falhou, valor informado inválido.")

        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

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


    elif opcao == "3":
        print ("########## EXTRATO ##########")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"Saldo: R$ {saldo:.2f}")
        print (f"Saques restantes hoje: {limite_saque_diario - numero_saques}")
        print ("#############################")


    elif opcao == "0":
        print ("\n Obrigado por utilizar nosso sistema! Volte sempre.")
        break
    else:
        print ("Opção inválida, por favor selecione novamente a operação desejada!")