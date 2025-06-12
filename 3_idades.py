idade = int(input("informe a idade: "))

if idade >= 0 and idade <=12 :
   
    print(f'eh criança de:{ idade} de idade'  )

elif idade >= 13 and idade <=17 :
   
    print(f'eh adolecente de:{ idade} de idade'  )

elif idade >= 18 and idade <=64 :
   
    print(f'eh adulto de:{ idade} de idade'  )

elif idade >= 65 :
   
    print(f'eh idoso de:{ idade} de idade'  )

else : 
  print( "Informação invalida")
    
