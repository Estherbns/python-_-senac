A = []

calculo = 0
for i in range(10):
    numero = int(input("informe o numero:"))

    A.append(numero)

for valor in A:
    if not(valor % 2 == 0):
        calculo = valor + calculo

          
print(calculo)
