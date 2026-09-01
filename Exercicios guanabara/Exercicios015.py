#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# De dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa $60 por dia 
# e R$0.15 por km rodado.
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km percorridos? "))
total = (dias * 60) + (km * 0.15)
print (f"O total a pagar é de: {total:.2f}R$")