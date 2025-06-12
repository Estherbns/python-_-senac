H = float(input("informe a altura: "))
sexo = str(input("informe o sexo ( F ou M ): "))

if sexo == "F" or sexo == "f":
    peso = (62.1 * H) - 44.7 
    print(f'o peso ideal é :{ peso:.3f}'  )
elif sexo =="M" or sexo == "m": 
     peso = (72.7 * H) - 58
     print(f'o peso ideal é :{ peso:.3f}'  )
else : 
   print( "digite novamente o sexo")