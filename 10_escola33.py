vetor = []
from EscolaFuncao import * # importa todas as funções do arquivo 
  
while True:
    op = int(input(" 1- cadastro\n 2- Listagem\n 9- Sair\n Informe a opção:"))
    match op:
        case 1:
            cadastrar (vetor)

        case 2:
             listagem(vetor)
                       
        case 9:
            print("Obrigado por acessar nosso programa.")
            break
        case _:
            print("Opção invalida")