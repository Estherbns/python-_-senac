vetor = []

while True:
    op = int(input(" 1- cadastro\n 2- Listagem\n 9- Sair\n Informe a opção:"))
    match op:
        case 1:
            aluno ={}
            aluno['nome'] = input(" informe o nome:")
            aluno['nota1'] = float(input(" informe nota1:"))
            aluno['nota2'] = float(input(" informe nota2:"))
            vetor.append(aluno)

        case 2:
            for a in vetor:
                media = (a['nota1'] + a['nota2'] ) / 2
                situacao = ''
                if media >=7:
                    situacao = "aprovado"
                else:
                    situacao = "reprovado" 

                print(f'{a["nome"]} - {a["nota1"]} - {a["nota2"]} - {media} - {situacao}')               
        case 9:
            print("Obrigado por acessar nosso programa.")
            break
        case _:
            print("Opção invalida")