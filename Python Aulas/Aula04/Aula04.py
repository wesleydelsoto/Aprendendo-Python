#Explicação sobre bibliotecas e modulos. 
# Uma biblioteca é um modulo adicional que vc pode importar para que seu programa rode.
# Ex: Para o corpo humano funcionar, ele precisa de alimentos, bebidas e doces entre outras coisas.
# Considerando que cada desses tópicos seja uma bibliotece em python, poderíamos importar-la da seguinte forma
# import bebida
# Porem ele iria importar todas as bebidas, e se quissessemos apenas uma biblioteca específica usaríamos:
# from bebida import café ( Da biblioteca bebida quero que importe o café)
# uma biblioteca comum e muito é ultilizada é a math . Algumas funcionalidades da biblioteca math.
# ceil - faz um arrendondamento para cima
# floor - faz um arrendondamento para baixo
# trunc - que é TRUNCATE - ele vai eliminar da virgula pra frente sem arrendondar 
# pow - potênciação
#sqrt - raiz quadrada
# factorial - para cacular a fatorial de um número 
# exemplos de uso : from math import sqrt - nesse exemplo so poderia usar a raiz quadrada.
# momento prático:
import math
num = int(input("Digite um número "))
raiz = math.sqrt (num)
print (f" A raiz de {num} é {math.ceil(raiz)}")   # Isso é ruim dms em questão de arrendondar, n use assim.