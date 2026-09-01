# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário com 15% de aumento
sal = float(input("Qual o salário do funcionário? R$"))
au = sal + (sal * 15/100 )
print (f"O salário que era R${sal:.2f} com o aumento de 15% ficou R${au:.2f}")