
nota1 = float(input("informe nota1: "))
nota2 = float(input("informe nota2: "))
media = (nota1 + nota2)/2
if media>= 7:
    print("Aluno aprovado")
    print( "A media da nota é :", media)
#elif media <= 6: 
    #print("Aluno reprovado")

else:
    recuperacao = float(input("nota de recuperação: "))
    nova_media = (media + recuperacao) / 2
    if nova_media >=5:
        print("Aluno aprovado")
        print( "A media da nota é :", nova_media)
    else:
        print("Aluno reprovado")
        print( "A media da nota é :", nova_media)


#print( "A media da nota é :", media) # uma das formas de aparecer o resultado da variavel é botando virgula após a mmsg