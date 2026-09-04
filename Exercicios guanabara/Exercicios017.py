# Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um traingulo retangulo
# calcule e mostre o comprimento da hipotenusa.
import math
ca1 = float(input("Qual o comprimento do cateto oposto? "))
ca2 = float(input("Qual o comprimento do cateto adjacente? "))
hi = math.hypot(ca1,ca2)
print (f" A hipotenusa vai medir {hi:.2f}")