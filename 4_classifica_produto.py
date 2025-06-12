cod_produto = int(input("informe o codigo do produto: "))


if cod_produto == 1 :
   
    print(f'{ cod_produto} - é alimento não perecível'  )

elif cod_produto == 2 or cod_produto == 3 or cod_produto == 4:
    print(f'{ cod_produto} - é alimento perecível'  )
   
elif cod_produto == 5 or cod_produto == 6 :
    print(f'{ cod_produto} - é vestuário'  )

elif cod_produto == 7 :
    print(f'{ cod_produto} - é higiene pessoal'  )

elif cod_produto == 8 or cod_produto == 9  or cod_produto == 10 :
    print(f'{ cod_produto} - é utensílio domestico'  )
 
else : 
  print( "código invalido")

  # ou usar o match  ******* só é usado quando eh o valor exato
  # match cod_produto:
      # case 1:
      #   print(f'{ cod_produto} - é alimento não perecível'  )
      # case 2 | 3 | 4:
      #    print(f'{ cod_produto} - é alimento perecível'  )
   # ...... etc
   #   case_:
   #      print( "código invalido")
   
  