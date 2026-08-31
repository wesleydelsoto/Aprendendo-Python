#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite a distância em metros "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m *100
mm = m *1000
print (f" A medida de {m} equivale a {km} km")
print (f" A medida de {m} equivale a {hm} hm")
print (f" A medida de {m} equivale a {dam} dam")
print (f" A medida de {m} equivale a {dm} dm")
print (f" A medida de {m} equivale a {cm} cm")
print (f" A medida de {m} equivale a {mm} mm")