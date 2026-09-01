#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 
#5% de desconto.
p = float(input("Digite o preço do produto R$ "))
d = p * 0.05
pf = p - d
print (f" O produto que custava {p} R$ com desconto custa {pf:.2f} R$")