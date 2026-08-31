#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
n1 = float(input("Digite sua primeira nota "))
n2 = float(input("Digite sua segunda nota "))
m = (n1+n2)/2
if (m>5):
    print ("Você foi aprovado")
else:
    print ("Você esta de recuperação")
print(f"Considerando sua 1ª nota {n1} e a 2ª nota {n2} A sua média é: \n {m} !")