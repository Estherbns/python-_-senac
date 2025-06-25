A = []
B = []
calculo = 0
for i in range(10):
    numero = int(input("informe o numero:"))

    A.append(numero)

for valor in A:
    if valor % 2 == 0:
        calculo = valor * 5
        B.append(calculo)
    else:
        calculo = valor + 5
        B.append(calculo)

print(B)