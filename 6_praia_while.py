# variaveis 
contador_praias_15km = 0
qtd_praias_nao_asfaltadas = 0
qtd_veranistas_pna = 0
continua = True
i = 0

# receber informacoes das praias
while continua == True:
    i = i+1    
    
    nome_praia = input(f'\nQual o nome da {i}a. praia: ')
    distancia_centro = float(input(f'Qual a distância do centro da {i}a. praia: '))
    numero_medio = int(input(f'Qual o número médio de veranistas da última temporada da {i}a. praia: '))
    tipo_acesso = int(input(f'Qual o tipo de acesso da {i}a. praia (0 - Não asfaltado / 1 - Asfaltado): '))

    # calcular numero praias +15km do centro
    if distancia_centro > 15:
        contador_praias_15km = contador_praias_15km + 1

    # descobrir e contar praias nao asfaltadas e acumular qtd media veranistas 
    if tipo_acesso == 0:
        qtd_praias_nao_asfaltadas = qtd_praias_nao_asfaltadas + 1
        qtd_veranistas_pna = qtd_veranistas_pna + numero_medio

    # O nome e a distância do centro, em km, de todas as praias de acesso 
    # asfaltado que tiveram menos de 1000 veranistas.
    if tipo_acesso == 1 and numero_medio < 1000:
        print("Praias com acesso asfaltado e menos de 1000 veranistas")
        #print("------------------------------------------------------")
        print("-"*54)
        print(nome_praia + " / " + f'{distancia_centro}km')

    resposta = input("Deseja informar outra praia (S-Sim / N-Não): ")
    if resposta == 'N':
        continua = False


#endwhile

# calcular qtd media de veranistas das praias não asfaltadas
if qtd_praias_nao_asfaltadas > 0:
    media_veranistas_pna = qtd_veranistas_pna / qtd_praias_nao_asfaltadas
else: 
    media_veranistas_pna = 0

print(f'Media Veranistas: {media_veranistas_pna}')
print(f'Praias a mais de 15km do centro: {contador_praias_15km}')





