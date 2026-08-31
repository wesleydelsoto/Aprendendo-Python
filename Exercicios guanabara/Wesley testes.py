nome = input("Digite seu nome ")
n1 = int(input(f"Digite um número {nome:=^20}! "))
n2 = int(input(f"Digite outro número {nome:=^20}! "))
s = n1+ n2
sub = n1 - n2
mult = n1*n2
di = n1//n2
po = n1**n2
d = n1/n2
print (f"A soma de {n1} e {n2} é {s}\nA subtração é {sub}\nA multiplicação é {mult} ")
print (f"A divisão inteira é {di} \nA potenciação é {po} \nA divisão é {d:.3f}", end=" ")
print (type(s))
print ("="*20)

