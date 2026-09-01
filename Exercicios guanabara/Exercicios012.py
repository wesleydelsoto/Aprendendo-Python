#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 
#5% de desconto.
p = float(input("Digite o preço do produto R$ "))
d = p * 0.05
pf = p - d
print (f" O produto que custava R${p:.2f} R$ com desconto de 5% custa {pf:.2f} R$")