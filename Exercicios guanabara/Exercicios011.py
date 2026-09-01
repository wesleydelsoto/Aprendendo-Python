#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua area
# e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta
# pinta uma area de 2m².
l = float(input("Digite a largura da parede "))
a = float(input("Digite a altura da parede "))
ar = l*a
tinta = ar/2
print (f"Sua parede tem a dimensão {l}x{a} e sua área é de {ar}m²")
print (f"Para pinta-la precisara de {tinta}l de tinta.")