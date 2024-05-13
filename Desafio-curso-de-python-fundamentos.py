import textwrap
def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito no valor: \tR$ {valor:.2f}\n"
        print ("=== Deposito realizado com sucesso. === \nVoltando para o menu...")
            
    else:
        print("@@@ Valor invalido, operacao falhou. @@@ \nVoltando para o menu...")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print("@@@ Voce nao possui saldo suficiente, operacao invalida.@@@ \nVoltando para o menu...")
            
    elif limite_excedido:
         print("@@@ Voce excedeu o limite, operacao invalida.@@@ \nVoltando para o menu...")
            
    elif saques_excedido:
        print("@@@Numero de saques permitidos excedido, operacao invalida.@@@ \nVoltando para o meunu...")
            
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque no valor: \tR$ {valor:.2f}\n"
        numero_saques += 1
        print ("=== Saque realizado com sucesso. === \nVoltando para o menu...")
    else:
        print ("@@@Valor informado invalidado, operacao invalida.@@@ \nVoltando para o menu...")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("=============EXTRATO=============")
    print("nao houve movimento bancario"if not extrato else extrato)
    print(f"Seu saldo: \t\tR${saldo:.2f}")
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")  
    usuario = filtrar_usuario(cpf, usuarios)  
    if usuario: 
        print("@@@ Usuario existente com o cpf informado. @@@ \nVoltando para o menu...")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuarios criado. === \nVoltando pra o menu")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada.=== \nVoltando pro menu...")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("@@@ Usuario nao encontrado.@@@ \nVoltando ao menu")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t {conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu ()

        if opcao == "d":
            valor = float(input("Digite o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                numero_saques= numero_saques,
                limite_saques= LIMITE_SAQUES,
            )   
           
        elif opcao == "e":
            exibir_extrato (saldo, extrato= extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
                
        elif opcao == "q":
            break

        else:
            print ("Operacao invalida, escolha uma opcao disponivel no menu, voltando ao menu...")

main()