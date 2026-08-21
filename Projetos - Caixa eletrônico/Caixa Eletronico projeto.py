nome = input("Qual o seu nome? ")
senha = input("Qual a sua senha? ")
saldo = 1000
if senha == "1234":
    print ("Acesso permitido!")
    print ("Bem vindo",nome)
    print ("Seu saldo é: ",saldo)
    opção = ""
    while opção !="4":
        print ("============CAIXA ELETRÔNICO ==================")
        print ("1 - Ver saldo")
        print ("2 - Sacar Dinheiro")
        print ("3 - Depositar dinheiro")
        print ("4 - Sair")
        opção = input("Escolha uma opção: ")

        if opção == "1":
            print ("Seu saldo é:",saldo)
        elif opção =="2" :
            valor = int(input("Qual o valor você desejaria sacar? "))
            saldo = saldo - valor
            print ("Seu novo saldo é: ",saldo)
        elif opção =="3":
            deposito = int(input("Quanto você deseja depositar? "))
            saldo = saldo + deposito
            print("Seu novo saldo é: ", saldo)
        elif opção =="4":
            print ("Obrigado por utilizar o caixa eletrônico!")
else:
    print ("Senha incorreta")
