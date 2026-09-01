# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
# quantos dólares ela pode comprar, considere : 1,00 = 3,27
c = float(input("Quanto dinheiro você tem n carteira? R$"))
d = c/3.27
print (f"Com R${c:.2f} você pode comprar U${d:.2f}")