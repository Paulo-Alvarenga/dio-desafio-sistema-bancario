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

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito no valor: R$ {valor:.2f}\n"
            print ("Voltando para o menu...")
        
        else:
            print("Valor invalido, operacao invalida, voltando para o menu...")
    
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Voce nao possui saldo suficiente, operacao invalida, voltando para o menu...")
        
        elif limite_excedido:
            print("Voce excedeu o limite, operacao invalida, voltando para o menu...")
        
        elif saques_excedido:
            print("Numero de saques permitidos excedido, operacao invalida, voltando para o meunu...")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print ("Valor informado invalidado, operacao invalida, voltando para o menu...")
    elif opcao == "e":
        print("====EXTRATO====")
        print("nao houve movimento bancario"if not extrato else extrato)
        print(f"Seu saldo: R${saldo:.2f}")
        print("===============")


    elif opcao == "q":
        break

    else:
        print ("Operacao invalida, escolha uma opcao disponivel no menu, voltando ao menu...")
