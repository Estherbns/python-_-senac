#salario / bonus / tempo de trab /  mostrar valor do bonus recebiso

salario = float(input("informe o salario: "))
tempo_trab = float(input("informe o tempo de trabalho: "))
bonus = None  # recebe nulo ou vazio

if tempo_trab >= 5 :
    
    salario_bonus = salario +(salario * 20/100) 
    bonus = salario * 20/100
   
    print(f'O salario com o bonus é { salario_bonus:.2f} '  )
    print(f'O  bonus é { bonus} '  )


else:
    salario_bonus = salario +(salario * 10/100) 
    bonus = salario * 10/100
   
    print(f'O salario com o bonus é { salario_bonus:.2f} '  )
    print(f'O  bonus é { bonus} '  )
