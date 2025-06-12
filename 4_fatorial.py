# nao entendi bem. 

fatorial = 1
saida = ' ' 
numero = int(input("informe o numero:"))

for i in range(numero, 0 , -1): 
    fatorial = fatorial * i
    saida = saida+str(i)
    if i !=1 :
      saida = saida+'.'
   
print(f"Fatorial do {numero}!= {saida}  = {fatorial}")
 