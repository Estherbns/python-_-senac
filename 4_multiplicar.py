# taboada

mult= 0
numero = float(input("informe o numero:"))

for contador in range(10): # range é especifico do python. No caso conta ate 5. de um em um. Começando por 0
# for contador in range(10, 17, 3):  - onde o 3 seria pular  de 3 em 3
# for contador in range(2, 8): - começa no segundo item ate 8. Pode tb colocar o contrario, de 8 a 2, No exemplo, abaixo
# for contador in range(8, 2, -1): - Pode tb colocar o contrario, reverso 
   J = contador +1
   resultado =  numero * J
  
 
  # print(f"A multiplicação é {resultado}")
   print(f" {numero} x {J} = {resultado}")