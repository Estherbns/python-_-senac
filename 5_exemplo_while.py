soma = 0
num_pessoa = 0

while True:
    idade = int(input(" informe a sua idade:"))
    soma = soma + idade
    num_pessoa = num_pessoa +1
    resp = input("deseja continuar? (s/n)")
    if resp == 'n' or resp == 'N':
        break # termina o while

media = soma / num_pessoa
print(f'O somatório das idades é {soma}')
print(f'numero de pessoas é {num_pessoa}')
print(f'a média das idades é {media:.2f}')
