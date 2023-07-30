menu = '''
Bem vindo! Informe a opção desejada:
    [1] Depositar
    [2] Sacar
    [3] Visualizar Extrato
    [4] Sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor: .2f}\n"

        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor maior do que saldo disponível.")

        elif excedeu_limite:
            print("O valor do saque excede limite.")
        
        elif excedeu_saque:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou. Valor informado é inválido.")

    elif opcao == "3":
        print("\n------------ EXTRATO -------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("----------------------------------")

    elif opcao == "4":
        break

    else:
        print("Opção inválida. Selecione opção desejada")
