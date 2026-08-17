idade = int(input("Qual a sua idade?"))
ingresso = input("Você possui ingresso?").lower()
if idade >=18 and ingresso == "sim":
    print ("Pode entrar")
else:
    print ("Não pode entrar!")
    
