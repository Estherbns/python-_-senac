tempo_viagem = float(input("informe tempo de viagem:"))
vel_media = float(input("informe velocidade média: "))


distancia_perco = tempo_viagem * vel_media

Qtd_litro_util = distancia_perco / 12



print(f'velocidade média { vel_media}'  )
print(f'Tempo de viagem { tempo_viagem} ' )
print(f'litros utilizados { Qtd_litro_util:.3f} ' )  #  :.3f - é a quantidade de casa decimais
