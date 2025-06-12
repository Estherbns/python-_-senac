
cod_lanche = 0
qtde = 0
valor = 0.0
Total=0.0
while True:
    cod_lanche = int(input(" informe o codigo do lanche:"))
    qtde = int(input(" informe a quantidade:"))
    if cod_lanche == 100:
      valor = 12 * qtde
      lanche = 'cachorro quente'
    elif cod_lanche == 103:
      valor = 12 * qtde
      lanche = 'hamburger'
    elif cod_lanche == 104:
      valor = 13 * qtde
      lanche = 'cheesburger'
    elif cod_lanche == 105:
      valor = 8 * qtde
      lanche = 'refrigerante'
    else: 
       print('codigo errado')
       continue # volta pro while

    Total = Total + valor
    print(f'O pedido  é {Total}')

    resp = input("deseja continuar? (s/n)")
    if resp == 'n' or resp == 'N':
        break # termina o while

   
   # print(f'O pedido  é {Total}')
