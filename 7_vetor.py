vetor = []
frutas = [ 'banana', 'pera', 'maça']

frutas.append("melão") # append é adicionar na lista
frutas.append("Luis")
vetor.append("Paulo")
frutas[0] = 'banana da terra'
frutas.insert(1,"açai") # tipo inclui linha, não substitui o dado dessa posição

print(frutas)
print(vetor)
print(frutas[1]) # vai mostrar o que está na posição/item 1 da lista fruta. Sendo que a lista sempre começa do 0 

frutas.remove("luis") # remove pelo valor
frutas.pop() # exclui a ultima linha ou voce pode digitar o numero da linha

try: # vai tentar fazer o comando ( tratamento de erro )
    frutas.remove("joão")
except:
    print("informação não encontrada")

frutas.sort() # ordena a lista em ordem crescente
#frutas.reverse() - ordena de ordem descrescente
#frutas.clear() # exclui tudo

for f in frutas: # vai entrar no f cada item da lista, rodando um em um
    print(f)



print("fim")