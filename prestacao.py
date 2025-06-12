valor = float(input("informe valor da prestação: "))
taxa = float(input("informe a taxa: "))
tempo = int(input("informe o tempo: "))

prestacao = valor +(valor * taxa/100) * tempo


print(f'valor da atualizado { prestacao:.2f}'  )
